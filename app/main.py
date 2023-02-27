from dotenv import load_dotenv
load_dotenv()
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, Response, status
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

@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
async def show(id: int, res: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No blog found with id of {id}")
    return blog

@app.post("/blog", status_code=status.HTTP_201_CREATED)
async def create_blog(req: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
