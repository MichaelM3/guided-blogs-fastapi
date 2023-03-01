from fastapi import APIRouter, Depends, status, HTTPException
from ..database import schemas, models, database
from ..database.crud import user
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserShow)
def show(id: int, db: Session = Depends(database.get_db)):
   return user.show(id, db) 

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserShow)
def create(req: schemas.UserBase, db: Session = Depends(database.get_db)):
    return user.create(req, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return user.destroy(id, db)
