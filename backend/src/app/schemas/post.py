from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class PostBase(BaseModel):
    title: str
    content: str


# Properties to receive via API on creation
class PostCreate(PostBase):
    pass


# Properties to receive via API on update
class PostUpdate(PostBase):
    pass


class PostInDBBase(PostBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Post(PostInDBBase):
    pass


# Additional properties stored in DB
class PostInDB(PostInDBBase):
    pass
