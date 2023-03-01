from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    body: str

class BlogShow(BlogBase):
    class Config:
        orm_mode = True

class BlogCreate(BlogBase):
    pass
    class Config:
        orm_mode = True

class BlogUpdate(BlogBase):
    title: Optional[str] = None
    body: Optional[str] = None
    class Config:
        orm_mode = True
