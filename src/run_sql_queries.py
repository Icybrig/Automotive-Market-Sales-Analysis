import pandas as pd
import psycopg2
import os
import yaml

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

postgre = config['database']

connection = psycopg2.connect(
    host=postgre['host'],
    port=postgre['port'],
    dbname=postgre['dbname'],
    user=postgre['user'],
    password=postgre['password']
)

cur = connection.cursor()

with open('sql/sql_queries.sql', 'r') as f:
    sql = f.read()

queries = sql.strip().split(';')

for i, query in enumerate(queries):
    query = query.strip()
    if query == "":
        continue
    cur.execute(query)
    try:
        rows = cur.fetchall()
        if rows:
            columns = [desc[0] for desc in cur.description]
            df = pd.DataFrame(rows, columns=columns)
            df.to_csv(f"outputs/sql_queries_results/query_result_{i+1}.csv", index=False)
            print(f"Query {i+1} has been executed and result saved into outputs/sql_queries_results/query_result_{i+1}.csv")
    except psycopg2.ProgrammingError:
        print(f"Executed successfully: {query}")

cur.close()
connection.close()