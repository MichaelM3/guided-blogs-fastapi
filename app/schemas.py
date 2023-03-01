from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

class BlogShow(BlogBase):
    pass

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BlogBase):
    title: Optional[str] = None
    body: Optional[str] = None

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserShow(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True
