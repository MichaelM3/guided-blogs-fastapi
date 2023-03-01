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
