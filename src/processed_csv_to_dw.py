import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from dw_connect import get_engine

# Import the processed Dataset
df = pd.read_csv("../data/processed/twitter_airlines_sentiment_processed.csv")


# Get the engine from connect
dw_engine = get_engine()


# Create DimAirline
df_airline = df[["airline"]].drop_duplicates()
df_airline["airline_id"] = range(1, len(df_airline)+1)
df_airline.to_sql('DimAirline', dw_engine, if_exists="replace", index=False)

# Create DimLocation
df_location = df[['tweet_location']].drop_duplicates()
df_location['location_id'] = range(1, len(df_location) + 1)
df_location.to_sql('DimLocation', dw_engine, if_exists='replace', index=False)

# Create DimDate
df['tweet_date'] = pd.to_datetime(df['tweet_created']).dt.date
df_date = df[['tweet_date']].drop_duplicates()
df_date['date_id'] = range(1, len(df_date) + 1)
df_date['year'] = pd.to_datetime(df_date['tweet_date']).dt.year
df_date['month'] = pd.to_datetime(df_date['tweet_date']).dt.month
df_date['day'] = pd.to_datetime(df_date['tweet_date']).dt.day
df_date.to_sql('DimDate', dw_engine, if_exists='replace', index=False)

# Create DimTime
df['tweet_time'] = pd.to_datetime(df['tweet_created']).dt.time
df_time = df[['tweet_time']].drop_duplicates()
df_time['time_id'] = range(1, len(df_time) + 1)
df_time['hour'] = pd.to_datetime(df_time['tweet_time'], format='%H:%M:%S').dt.hour
df_time['minute'] = pd.to_datetime(df_time['tweet_time'], format='%H:%M:%S').dt.minute
df_time.to_sql('DimTime', dw_engine, if_exists='replace', index=False)

# Create DimSentiment
df_sentiment = df[['airline_sentiment']].drop_duplicates()
df_sentiment['sentiment_id'] = range(1, len(df_sentiment) + 1)
df_sentiment.to_sql('DimSentiment', dw_engine, if_exists='replace', index=False)

print("Dimension tables created successfully.")


# Prepare the fact Table
df_fact = df.merge(df_airline, on= 'airline')
df_fact = df_fact.merge(df_date, on='tweet_date')
df_fact = df_fact.merge(df_time, on='tweet_time')
df_fact = df_fact.merge(df_sentiment, on='airline_sentiment')
df_fact = df_fact.merge(df_location, on='tweet_location')

# Select columns for the fact table
fact_columns = ['airline_id', 'date_id', 'time_id', 'sentiment_id', 'location_id', 'negativereason',
                'retweet_count', 'text', 'cleaned_text']
df_fact = df_fact[fact_columns]

# Create the fact table
df_fact.to_sql('FactAirlineSentiment', dw_engine, if_exists='replace', index=False)

print("Fact table created successfully.")

# Create Table Relations
with dw_engine.connect() as conn:
    try:
        trans = conn.begin()  # Begin a transaction

        conn.execute(text("ALTER TABLE \"DimAirline\" ADD PRIMARY KEY (airline_id)"))
        conn.execute(text("ALTER TABLE \"DimDate\" ADD PRIMARY KEY (date_id)"))
        conn.execute(text("ALTER TABLE \"DimTime\" ADD PRIMARY KEY (time_id)"))
        conn.execute(text("ALTER TABLE \"DimSentiment\" ADD PRIMARY KEY (sentiment_id)"))
        conn.execute(text("ALTER TABLE \"DimLocation\" ADD PRIMARY KEY (location_id)"))
        conn.execute(text("ALTER TABLE \"FactAirlineSentiment\" ADD FOREIGN KEY (airline_id) REFERENCES \"DimAirline\" (airline_id)"))
        conn.execute(text("ALTER TABLE \"FactAirlineSentiment\" ADD FOREIGN KEY (date_id) REFERENCES \"DimDate\" (date_id)"))
        conn.execute(text("ALTER TABLE \"FactAirlineSentiment\" ADD FOREIGN KEY (time_id) REFERENCES \"DimTime\" (time_id)"))
        conn.execute(text("ALTER TABLE \"FactAirlineSentiment\" ADD FOREIGN KEY (sentiment_id) REFERENCES \"DimSentiment\" (sentiment_id)"))
        conn.execute(text("ALTER TABLE \"FactAirlineSentiment\" ADD FOREIGN KEY (location_id) REFERENCES \"DimLocation\" (location_id)"))
        
        trans.commit()  # Commit the transaction
        
        print("Primary and foreign key constraints added successfully.")

    except SQLAlchemyError as e:
        trans.rollback()
        print(f"Transaction failed: {e}")
