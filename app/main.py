from dotenv import load_dotenv
load_dotenv()
from fastapi import Depends, FastAPI, HTTPException, status
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
def index(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id was not found!")
    return blog

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(req: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, req: schemas.BlogUpdate, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id was not found!")
    for key, value in req.dict(exclude_unset=True).items():
        setattr(blog, key, value)
    db.commit()
    db.refresh(blog)
    return blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id was not found!")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog was deleted"


