import psycopg2
from psycopg2.extras import RealDictCursor
import logging

config_deault = {
        'host': '172.22.0.40',
        'database': 'metrics',
        'user': 'admin',
        'password': 'admin123',
        'port': 5432
    }

class DatabaseClient:
    def __init__(self, config = config_deault):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.test_connection()

    def execute(self, query: str) -> (list, str):
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(query)
                    rows = [dict(r) for r in cur.fetchall()]
                    return rows, "Sucesso"
        except Exception as e:
            self.logger.error(f"Erro SQL: {e}")
            return [], str(e)

    def test_connection(self):
        try:
            self.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        except Exception as e:
            print(e)
# db = DatabaseClient(config=config)
# query = '''
# SELECT table_name FROM information_schema.tables WHERE table_schema='public' 
# '''
# db.execute(query)