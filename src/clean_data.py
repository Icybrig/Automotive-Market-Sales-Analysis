import pandas as pd
import os
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

raw_car_path = config['paths']['raw_car_data']
raw_consumer_path = config['paths']['raw_consumer_data']
cleaned_car_path = config['paths']['cleaned_car_data']
cleaned_consumer_path = config['paths']['cleaned_consumer_data']

car_df = pd.read_csv(raw_car_path )

def clean_col_name(col):
    col = col[1:-1].split(',')[0].strip().strip("'")
    return col.lower().replace(' ', '_')

car_df.columns = [clean_col_name(col) for col in car_df.columns]

car_df.dropna(inplace = True)

car_df['price'] = car_df['price'].astype(float)
car_df['year'] = car_df['year'].astype(int)

car_df.to_csv(cleaned_car_path, index = False)
print(f'car data has been cleaned')

consumer_df = pd.read_csv(raw_consumer_path)

consumer_df.columns = [col.strip().lower().replace(' ', '_') for col in consumer_df.columns]

consumer_df.dropna(inplace = True)

consumer_df['review_score'] = consumer_df['review_score'].astype(float)
consumer_df['year'] = consumer_df['year'].astype(int)
consumer_df['sales_volume'] = consumer_df['sales_volume'].astype(int)

consumer_df.to_csv(cleaned_consumer_path, index = False)
print(f'consumer data has been cleaned')