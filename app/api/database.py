from dotenv import load_dotenv
load_dotenv()
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL variable found in .env")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

