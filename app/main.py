from dotenv import load_dotenv
load_dotenv()
from typing import Optional
from fastapi import Depends, FastAPI
from .api import database, models, schemas
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/blog")
async def index(limit: int = 10, sort: Optional[str] = None, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}")
async def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog

@app.get("/blog/{id}/comments")
async def comments(id: int, limit: int = 10):
    return { "data": {"1", "2"} }

@app.post("/blog", status_code=201)
async def create_blog(req: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
