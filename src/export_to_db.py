import pandas as pd 
import psycopg2
import yaml

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
postgre = config['database']

car_df = pd.read_csv('data/cleaned/cleaned_car_data.csv')
consumer_df = pd.read_csv('data/cleaned/cleaned_consumer_data.csv')

def insert_df(df, table_name):
    connection = psycopg2.connect(
        host=postgre["host"],
        port=postgre["port"],
        dbname=postgre["dbname"],
        user=postgre["user"],
        password=postgre["password"]
    )
    cur = connection.cursor()
 
    columns = ','.join(df.columns)
    placeholders = ', '.join(['%s'] * len(df.columns))

    for _, row in df.iterrows():
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cur.execute(sql, tuple(row))

    connection.commit()
    cur.close()
    connection.close()

insert_df(car_df, postgre['car_table'])
insert_df(consumer_df, postgre['consumer_table'])

print('data has been imported into postgresql database')