from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from . import database, models

app = FastAPI()

models.Base.metadata.create_all(database.engine)

