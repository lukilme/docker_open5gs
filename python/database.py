import psycopg2
import pandas as pd
from metrics_dict import metrics_dict

connection = psycopg2.connect(
        host="172.22.0.40",
        port=5432,
        database="metrics",
        user="admin",
        password="admin123"
        )

cur = connection.cursor()

cur.execute("""
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_type = 'BASE TABLE'
        AND table_schema NOT IN ('pg_catalog', 'information_schema')
""")

cur.execute("""
    SELECT * FROM gnb;
""")


result = cur.fetchall()
for index in result:
    print(index)
# print("Tabelas disponiveis:")
# for schema, table in cur.fetchall():
#     print(f"{schema}.{table}")

column_names = list(metrics_dict.keys())

df = pd.DataFrame(columns=column_names)

df_helper = pd.DataFrame(columns=["name","help","type"])
for name in column_names:
    aux = pd.DataFrame({'name':[name],'help':[metrics_dict[name]['help']], 'type':[metrics_dict[name]['type']]})
    df_helper = pd.concat([df_helper, aux], ignore_index=True)
print(df_helper)
cur.close()
connection.close()



