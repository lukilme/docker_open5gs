import os
import json
import time
from kafka import KafkaConsumer
from datetime import datetime
import psycopg2

# Cores ANSI para logs
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

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
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                host=DB_HOST,
                port=DB_PORT
            )
            print(Color.GREEN + "Conectado ao PostgreSQL" + Color.RESET)
            return conn
        except psycopg2.OperationalError as e:
            print(Color.YELLOW + f"PostgreSQL ainda não disponível ({attempt+1}/{max_retries}): {e}" + Color.RESET)
            time.sleep(delay)
    raise Exception("Falha ao conectar ao PostgreSQL após várias tentativas")

def wait_for_kafka(broker, topic, timeout=60):
    print(Color.CYAN + f"Conectando ao Kafka em {broker}, tópico {topic}" + Color.RESET)
    start = time.time()
    while time.time() - start < timeout:
        try:
            test_consumer = KafkaConsumer(
                topic,
                bootstrap_servers=broker,
                consumer_timeout_ms=3000
            )
            test_consumer.close()
            print(Color.GREEN + "Kafka disponível!" + Color.RESET)
            return
        except:
            print(Color.YELLOW + "Aguardando Kafka..." + Color.RESET)
            time.sleep(2)
    raise Exception("Kafka não respondeu a tempo.")

conn = wait_for_postgres()
cursor = conn.cursor()
wait_for_kafka(KAFKA_BROKER, KAFKA_TOPIC)

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
    "softmodern_rsrp",
    "pfcp_sessions_active"
]

message_count = 0

for message in consumer:
    message_count += 1
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
        fields = metric.get("fields", {})
        raw_value = fields.get("counter", fields.get("gauge", 0))

        try:
            value = int(raw_value)
        except (ValueError, TypeError):
            value = 0

        if not name or name not in ALL_METRICS:
            continue

        cursor.execute("SELECT 1 FROM metric WHERE time = %s", (ts,))
        exists = cursor.fetchone() is not None

        if not exists:
            values_dict = {col: 0 for col in ALL_METRICS}
            values_dict[name] = value

            columns = ', '.join(['time'] + list(values_dict.keys()))
            placeholders = ', '.join(['%s'] * (len(values_dict) + 1))
            values = [ts] + list(values_dict.values())

            sql = f"INSERT INTO metric ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, values)
        else:
            sql = f"UPDATE metric SET {name} = %s WHERE time = %s"
            cursor.execute(sql, (value, ts))  

        conn.commit()
        print(f"{Color.BLUE}[{message_count:05}]{Color.GREEN} {name} @ {ts} → {value}{Color.RESET}")

    except Exception as e:
        conn.rollback()
        print(f"{Color.RED}[{message_count:05}] ❌ Erro ao processar mensagem: {e}{Color.RESET}")
