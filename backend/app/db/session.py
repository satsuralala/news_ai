from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql+psycopg2://fastapi_user:FastApi@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

try:
    with engine.connect() as connection:
        print("✅ Successfully connected to PostgreSQL")
except OperationalError as e:
    print("❌ Could not connect to PostgreSQL")
    print("Error:", e)
