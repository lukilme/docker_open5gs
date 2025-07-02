import psycopg2
from pymongo import MongoClient
from datetime import datetime, timedelta

def diagnose_plmn_error():
    ts_conn = psycopg2.connect(
        host="172.22.0.40",
        database="metrics",
        user="admin",
        password="admin123"
    )
    
    mongo_client = MongoClient('mongodb://172.22.0.10:27017/')
    db = mongo_client.open5gs
    
    report = []
    try:
        ue_imsi = "001010000000001"
        subscriber = db.subscribers.find_one({"imsi": ue_imsi})
        
        if not subscriber:
            report.append("CRITICAL: UE subscription missing in UDM database")
            report.append(f"  → IMSI {ue_imsi} not found")
            report.append("  Solution: docker exec -it open5gs-amf open5gs-dbctl add 001010000000001 KEY")
        else:
            report.append(f"UE subscription found for IMSI: {ue_imsi}")
            
        with ts_conn.cursor() as cur:
            cur.execute("""
                SELECT COUNT(*) 
                FROM fivegs_amffunction_rm_reginitreq
                WHERE time > NOW() - INTERVAL '5 minutes'
            """)
            reg_attempts = cur.fetchone()[0]

            cur.execute("""
                SELECT COUNT(*) 
                FROM fivegs_amffunction_rm_reginitfail
                WHERE time > NOW() - INTERVAL '5 minutes'
            """)
            reg_failures = cur.fetchone()[0]
            
            report.append(f"Registration attempts (last 5min): {reg_attempts}")
            report.append(f"Registration failures (last 5min): {reg_failures}")
            
            if reg_attempts > 0 and reg_failures == reg_attempts:
                report.append("  → 100% failure rate on registrations")
                
    finally:
        ts_conn.close()
        mongo_client.close()
    
    return "\n".join(report)

def check_amf_configuration():
    """Verificar configuração do AMF via Docker (simulação)"""
    return """
AMF configuration check (simulated):
  - PLMN Support: 
      mcc: '001'
      mnc: '01'
      Status: OK
  - Network Slices:
      SST: 1, SD: None
      Status: Active
"""

if __name__ == "__main__":
    print("=== UE Registration Failure Diagnosis ===")
    print(diagnose_plmn_error())
    print("\n=== AMF Configuration Check ===")
    print(check_amf_configuration())
    print("\nRecommended Actions:")
    print("1. Verify PLMN in AMF config (amf.yaml)")
    print("2. Check UE subscription in MongoDB")
    print("3. Ensure UE config matches AMF PLMN")