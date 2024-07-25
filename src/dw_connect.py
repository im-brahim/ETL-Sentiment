from sqlalchemy import create_engine

db_info = {
    "db_username" : 'dwuser',
    "db_password" : 'dw',
    "db_host" : 'localhost',
    "db_port" : '5433',
    "db_name" : 'airline_sentiment_dw'
}

def get_engine(): 
    engine = create_engine(f'postgresql://{db_info["db_username"]}:{db_info["db_password"]}@{db_info["db_host"]}:{db_info["db_port"]}/{db_info["db_name"]}')
    return engine