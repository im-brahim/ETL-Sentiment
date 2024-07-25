import pandas as pd
from db_connect import get_engine

# Get the engine from connect
engine = get_engine()

# Read the CSV file
df = pd.read_csv("../data/raw/twitter_airlines_sentiment.csv", encoding='ISO-8859-1')

# Import the raw data into PostgreSQL
table_name = 'airline_sentiment'
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Data imported successfully into table: {table_name}")