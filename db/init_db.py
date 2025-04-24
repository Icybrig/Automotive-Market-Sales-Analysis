import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:Fly140401.@localhost:5432/car_db")

car_df = pd.read_csv('data/car_data.csv')
consumer_df = pd.read_csv('data/consumer_data.csv')

car_df.to_sql('car_data', engine, if_exist = 'replace', index = False)
consumer_df.to_sql('consumer_data', engine, if_exist = 'replace', index = False)

print('data has been imported into the database')