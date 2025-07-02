import psycopg2
import pandas as pd
from datetime import datetime, timedelta
from metrics_dict import metrics_dict

# Conexão com o TimescaleDB
def connect_db():
    return psycopg2.connect(
        host="172.22.0.40",
        port=5432,
        database="metrics",
        user="admin",
        password="admin123"
    )

# Identificar métricas críticas baseado no contexto
CRITICAL_METRICS = [
    "ran_ue",                          # UEs conectadas ao RAN
    "ues_active",                      # UEs ativas no sistema
    "fivegs_amffunction_rm_reginitsucc", # Registros iniciais bem-sucedidos
    "fivegs_smffunction_sm_pdusessioncreationsucc", # Sessões PDU criadas
    "bearers_active",                  # Portadoras ativas
    "fivegs_amffunction_rm_reginitfail", # Falhas no registro inicial
    "fivegs_ep_n3_gtp_indatapktn3upf", # Pacotes de dados recebidos (N3)
    "fivegs_amffunction_amf_authfail", # Falhas de autenticação
    "fivegs_amffunction_rm_regmobsucc" # Handovers bem-sucedidos
]

# Coletar dados das métricas críticas
def fetch_critical_metrics(connection):
    try:
        cur = connection.cursor()
        results = {}
        
        for metric in CRITICAL_METRICS:
            try:
                # Buscar último valor e timestamp
                cur.execute(f"""
                    SELECT time, value 
                    FROM {metric}
                    ORDER BY time DESC 
                    LIMIT 1
                """)
                row = cur.fetchone()
                
                if row:
                    results[metric] = {
                        'last_value': row[1],
                        'last_timestamp': row[0]
                    }
                else:
                    results[metric] = {
                        'last_value': None,
                        'last_timestamp': None
                    }
                    
            except psycopg2.Error as e:
                print(f"Erro na métrica {metric}: {e}")
                results[metric] = {
                    'last_value': None,
                    'last_timestamp': None
                }
                
        return results
        
    finally:
        cur.close()

# Gerar relatório de saúde da rede
def generate_health_report(metrics_data):
    report = []
    
    # Verificar métricas essenciais
    ue_connected = metrics_data.get('ran_ue', {}).get('last_value', 0) or 0
    reg_success = metrics_data.get('fivegs_amffunction_rm_reginitsucc', {}).get('last_value', 0) or 0
    pdu_success = metrics_data.get('fivegs_smffunction_sm_pdusessioncreationsucc', {}).get('last_value', 0) or 0
    
    # Critérios de saúde
    status = "HEALTHY"
    if ue_connected == 0:
        status = "CRITICAL - No UEs connected"
    elif reg_success == 0:
        status = "WARNING - No successful registrations"
    elif pdu_success == 0:
        status = "WARNING - No PDU sessions established"
    
    # Construir relatório
    report.append(f"=== Network Health Status ===")
    report.append(f"Status: {status}")
    report.append(f"Timestamp: {datetime.utcnow().isoformat()}Z")
    report.append("\nKey Metrics:")
    
    for metric in CRITICAL_METRICS:
        data = metrics_data.get(metric, {})
        report.append(
            f"- {metric}: {data.get('last_value', 'N/A')} "
            f"(at {data.get('last_timestamp', 'N/A')})"
        )
    
    return "\n".join(report)

# Coletar dados históricos para análise
def fetch_historical_data(connection, metric_name, hours=24):
    try:
        cur = connection.cursor()
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(hours=hours)
        
        cur.execute(f"""
            SELECT time_bucket('1 hour', time) AS period,
                   AVG(value) as avg_value,
                   MAX(value) as max_value
            FROM {metric_name}
            WHERE time > %s
            GROUP BY period
            ORDER BY period
        """, (start_time,))
        
        df = pd.DataFrame(
            cur.fetchall(),
            columns=['period', 'avg_value', 'max_value']
        )
        df['metric'] = metric_name
        return df
        
    finally:
        cur.close()

# Main
if __name__ == "__main__":
    conn = connect_db()
    
    # 1. Coletar métricas críticas
    critical_data = fetch_critical_metrics(conn)
    
    # 2. Gerar relatório de saúde
    health_report = generate_health_report(critical_data)
    print(health_report)
    
    # 3. Exemplo: Análise histórica de métrica específica
    ran_ue_value = critical_data.get('ran_ue', {}).get('last_value')
    if isinstance(ran_ue_value, (int, float)) and ran_ue_value > 0:
        historical_df = fetch_historical_data(conn, 'ran_ue')
        print("\nHistorical UE Connection Data:")
        print(historical_df.head())
    
    conn.close()