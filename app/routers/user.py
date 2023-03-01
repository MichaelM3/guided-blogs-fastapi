from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
from ..hashing import bcrypt
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserShow)
def show(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with this id was not found!")
    return user

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserShow)
def create(req: schemas.UserBase, db: Session = Depends(database.get_db)):
    new_user = models.User(name=req.name, email=req.email, password=bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.UserBase)
def update(id: int, req: schemas.BlogUpdate, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with this id was not found!")
    for key, value in req.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with this id was not found!")
    user.delete(synchronize_session=False)
    db.commit()
    return "User was deleted"
