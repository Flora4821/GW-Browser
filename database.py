from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+mysqlconnector://root:MarioCesar5+@localhost/gwarchive", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)

Base = declarative_base()

def execute_query(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
    return result.fetchall()
