import os
from kafka import KafkaConsumer
import json
import psycopg2
from datetime import datetime
import time
import psycopg2
import os


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "metrics")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASS", "admin123")
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "prometheus_metrics")


def wait_for_postgres(max_retries=10, delay=5):
    for attempt in range(max_retries):
        try:
            conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            print("✅ Conectado ao PostgreSQL")
            return conn
        except psycopg2.OperationalError as e:
            print(f"⏳ PostgreSQL ainda não disponível ({attempt+1}/{max_retries}): {e}")
            time.sleep(delay)
    raise Exception("❌ Falha ao conectar ao PostgreSQL após várias tentativas")

conn = wait_for_postgres()
cursor = conn.cursor()
from kafka.errors import NoBrokersAvailable

def wait_for_kafka(broker, timeout=60):
    print(f"⏳ Aguardando Kafka ({broker}) ficar disponível...")
    start = time.time()
    while time.time() - start < timeout:
        try:
            consumer = KafkaConsumer(
                KAFKA_TOPIC,
                bootstrap_servers=broker,
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                group_id='metrics-group',
                value_deserializer=lambda x: x.decode('utf-8'),
                consumer_timeout_ms=1000
            )
            consumer.close()
            print("✅ Kafka disponível!")
            return
        except NoBrokersAvailable as e:
            print("❌ Kafka ainda não está pronto. Tentando novamente...")
            time.sleep(2)
    raise Exception("❌ Kafka não ficou disponível a tempo.")
wait_for_kafka(KAFKA_BROKER)
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='metrics-group',
    value_deserializer=lambda x: x.decode('utf-8')
)
import os
import json
import time
from kafka import KafkaConsumer
from datetime import datetime
import psycopg2

# Configs do ambiente
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "metrics")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASS", "admin123")
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "prometheus_metrics")

# Conexão com o PostgreSQL
def wait_for_postgres(max_retries=10, delay=5):
    for attempt in range(max_retries):
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                host=DB_HOST,
                port=DB_PORT
            )
            print("✅ Conectado ao PostgreSQL")
            return conn
        except psycopg2.OperationalError as e:
            print(f"⏳ PostgreSQL ainda não disponível ({attempt+1}/{max_retries}): {e}")
            time.sleep(delay)
    raise Exception("❌ Falha ao conectar ao PostgreSQL após várias tentativas")

conn = wait_for_postgres()
cursor = conn.cursor()

# Espera Kafka estar pronto
def wait_for_kafka(broker, topic, timeout=60):
    print(f"🔌 Conectando ao Kafka em {broker}, tópico {topic}")
    start = time.time()
    while time.time() - start < timeout:
        try:
            test_consumer = KafkaConsumer(
                topic,
                bootstrap_servers=broker,
                consumer_timeout_ms=3000
            )
            test_consumer.close()
            print("✅ Kafka disponível!")
            return
        except:
            print("⏳ Aguardando Kafka...")
            time.sleep(2)
    raise Exception("❌ Kafka não respondeu a tempo.")

wait_for_kafka(KAFKA_BROKER, KAFKA_TOPIC)

# Consumer real
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='metrics-group',
    value_deserializer=lambda x: x.decode('utf-8')
)
ALL_METRICS = [
    "fivegs_amffunction_rm_registeredsubnbr",
    "fivegs_amffunction_rm_regmobreq",
    "fivegs_amffunction_rm_regmobsucc",
    "fivegs_amffunction_rm_regmobfail",
    "fivegs_smffunction_sm_sessionnbr",
    "fivegs_smffunction_sm_pdusessioncreationreq",
    "fivegs_smffunction_sm_pdusessioncreationsucc",
    "fivegs_ep_n3_gtp_indatapktn3upf",
    "fivegs_ep_n3_gtp_outdatapktn3upf",
    "fivegs_upffunction_upf_sessionnbr",
    "fivegs_smffunction_upf_qos_flow_nbr",
    "fivegs_upffunction_sm_n4sessionreport",
    "fivegs_upffunction_sm_n4sessionreportsucc",
    "fivegs_upffunction_sm_n4sessionestabreq",
    "fivegs_upffunction_sm_n4sessionestabfail",
    "softmodern_bler_dl",
    "softmodern_bler_ul",
    "softmodern_rsrp"
]


for message in consumer:
    print(f"Mensagem recebida: {message.value}")
    try:
        metric = json.loads(message.value)

        ts_raw = metric["timestamp"]
        if isinstance(ts_raw, int):
            ts = datetime.fromtimestamp(ts_raw)
        elif isinstance(ts_raw, str):
            ts = datetime.strptime(ts_raw, "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            raise ValueError("Formato de timestamp inválido.")

        name = metric.get("name")
        counter = int(metric.get("fields", {}).get("counter", 0))

        if not name or name not in ALL_METRICS:
            print(f"[⚠️] Métrica '{name}' desconhecida ou ausente. Ignorando.")
            continue

        # Verifica se já existe entrada para esse timestamp
        cursor.execute("SELECT 1 FROM metric WHERE time = %s", (ts,))
        exists = cursor.fetchone() is not None

        if not exists:
            # Cria um dicionário com todas as colunas zeradas
            values_dict = {col: 0 for col in ALL_METRICS}
            values_dict[name] = counter

            columns = ', '.join(['time'] + list(values_dict.keys()))
            placeholders = ', '.join(['%s'] * (len(values_dict) + 1))
            values = [ts] + list(values_dict.values())

            sql = f"INSERT INTO metric ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, values)
        else:
            # Atualiza apenas a métrica específica
            sql = f"""
            UPDATE metric
            SET {name} = %s
            WHERE time = %s
            """
            cursor.execute(sql, (counter, ts))

        conn.commit()
        print(f"[✔] {name} @ {ts} → {counter}")

    except Exception as e:
        conn.rollback()
        print(f"[✘] Erro: {e}")
