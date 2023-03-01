from pydantic import BaseModel
from typing import Optional, List

class BlogBase(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserShow(BaseModel):
    name: str
    email: str
    blogs: List[BlogBase] = []
    class Config:
        orm_mode = True

class BlogShow(BlogBase):
    user: UserShow

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BlogBase):
    title: Optional[str] = None
    body: Optional[str] = None
