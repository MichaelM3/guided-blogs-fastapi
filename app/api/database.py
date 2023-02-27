from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
import os

DATABASE_URL: str = os.getenv("DATABASE_URL") or ""
engine = create_engine(DATABASE_URL)


