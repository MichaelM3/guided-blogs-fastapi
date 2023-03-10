from fastapi import FastAPI
from .database import database, models
from .routers import blog, user, auth

app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)
