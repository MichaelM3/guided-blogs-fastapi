from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status, HTTPException
from ..hashing import bcrypt

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with this id was not found!")
    return user

def create(req: schemas.UserBase, db: Session):
    new_user = models.User(name=req.name, email=req.email, password=bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def destroy(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with this id was not found!")
    user.delete(synchronize_session=False)
    db.commit()
    return "User was deleted"
