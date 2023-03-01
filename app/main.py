from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from . import database, models
from .routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(blog.router)
app.include_router(user.router)
