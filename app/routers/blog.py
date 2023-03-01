from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.BlogShow])
def index(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.BlogShow)
def show(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id was not found!")
    return blog

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.BlogShow)
def create(req: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.BlogUpdate)
def update(id: int, req: schemas.BlogUpdate, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id was not found!")
    for key, value in req.dict(exclude_unset=True).items():
        setattr(blog, key, value)
    db.commit()
    db.refresh(blog)
    return blog

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id was not found!")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog was deleted"
