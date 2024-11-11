import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load the env variables
load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

# Set up the SQLAlchemy engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=10,             # Maximum number of connections in the pool
    max_overflow=20,           # Extra connections allowed when the pool is full
    pool_timeout=30,           # Timeout for getting a connection from the pool
    pool_recycle=1800          # Recycle connections every 30 minutes
)

# SessionLocal will create a new session when called, tied to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide the session to the request handler
    finally:
        db.close()  # Close the session after the request