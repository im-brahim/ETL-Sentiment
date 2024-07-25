from sqlalchemy import create_engine

db_info = {
    "db_username" : 'dbuser',
    "db_password" : 'db',
    "db_host" : 'localhost',
    "db_port" : '5432',
    "db_name" : 'airline_sentiment_db'
}

def get_engine(): 
    engine = create_engine(f'postgresql://{db_info["db_username"]}:{db_info["db_password"]}@{db_info["db_host"]}:{db_info["db_port"]}/{db_info["db_name"]}')
    return engine