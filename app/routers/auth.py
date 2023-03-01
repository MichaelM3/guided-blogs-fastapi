from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .token import create_access_token
from ..database import schemas, database, models
from ..database.hashing import Hash

router = APIRouter(
        tags=["Auth"]
)

@router.post("/login")
def login(req: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == req.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
