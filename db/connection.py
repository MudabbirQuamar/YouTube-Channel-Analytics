import os 
from dotenv import load_dotenv
from  sqlalchemy import create_engine

load_dotenv() # this loads the .env file to the environment variable

def get_engine():
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")

    '''print(f"User: '{DB_USER}'")
    print(f"Password: '{DB_PASSWORD}'")
    print(f"Host: '{DB_HOST}'")
    print(f"Database: '{DB_NAME}'")'''

    #creating engine to connect to postgre database
    return create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",future=True, isolation_level="AUTOCOMMIT")

#checcking the connection if is is successful
def check_connection(engine):
    with engine.connect() as conn:
        result = conn.execute("select version();")
        for rows in result:
            print(rows)

if __name__ == "__main__":
    engine= get_engine()
    check_connection(engine)

