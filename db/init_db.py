import yaml 
import psycopg2

with open('config/config.yaml','r') as file:
    config = yaml.safe_load(file)

postgre = config['database']

connection = psycopg2.connect(
    host = postgre['host'],
    port=postgre['port'],
    dbname=postgre['dbname'],
    user=postgre['user'],
    password=postgre['password']
)
cur = connection.cursor()

create_car_table = f"""
CREATE TABLE IF NOT EXISTS {postgre['car_table']} (
    id SERIAL PRIMARY KEY,
    make TEXT,
    model TEXT ,
    production_year INT,
    price FLOAT,
    engine_type TEXT
);
"""

create_consumer_table = f"""
CREATE TABLE IF NOT EXISTS {postgre['consumer_table']} (
    id SERIAL PRIMARY KEY,
    country TEXT,
    brand TEXT,
    model TEXT,
    year INT,
    review_score FLOAT,
    sales_volume INT
);
"""

cur.execute(create_car_table)
cur.execute(create_consumer_table)

connection.commit()
cur.close()
connection.close()

print('database and table structure has been created')