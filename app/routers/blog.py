from fastapi import APIRouter, Depends, status, HTTPException
from ..database import schemas, models, database
from ..database.crud import blog
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.BlogShow])
def index(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.BlogShow)
def show(id: int, db: Session = Depends(database.get_db)):
    return blog.show(id, db)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.BlogShow)
def create(req: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    return blog.create(req, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.BlogUpdate)
def update(id: int, req: schemas.BlogUpdate, db: Session = Depends(database.get_db)):
    return blog.update(id, req, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return blog.destroy(id, db)
