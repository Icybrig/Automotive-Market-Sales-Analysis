from fastapi import FastAPI
import psycopg2
import pandas as pd
import yaml
from fastapi.responses import JSONResponse

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

postgre = config['database']

def get_connection():
    connection = psycopg2.connect(
        host=postgre['host'],
        port=postgre['port'],
        dbname=postgre['dbname'],
        user=postgre['user'],
        password=postgre['password']
    )
    return connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running and can connect to PowerBI"}

@app.get("/car_data")
def get_car_data():
    connection = get_connection()
    query = f"SELECT * FROM {postgre['car_table']};"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return JSONResponse(content=df.to_dict(orient="records"))

@app.get("/consumer_data")
def get_consumer_data():
    connection = get_connection()
    query = f"SELECT * FROM {postgre['consumer_table']};"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return JSONResponse(content=df.to_dict(orient="records"))