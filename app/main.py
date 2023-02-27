from typing import Optional
from fastapi import FastAPI
from api.schemas import Blog

app = FastAPI()

@app.get("/blog")
async def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published: 
        return { "data": f"{limit} published blogs from the db" }
    return { "data": f"{limit} blogs from the db" }

@app.get("/blog/unpublished")
async def unpublished():
    return { "data": "All unpublished blogs" }

@app.get("/blog/{id}")
async def show(id: int):
    return { "data": {id} }

@app.get("/blog/{id}/comments")
async def comments(id: int, limit: int = 10):
    return { "data": {"1", "2"} }

@app.post("/blog")
async def create_blog(blog: Blog):
    return { "data": f"Blog is created with title {blog.title}!" }
