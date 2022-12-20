from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


# Shared properties
class CommentBase(BaseModel):
    user_id: int
    post_id: int
    content: str


# Properties to receive via API on creation
class CommentCreate(CommentBase):
    pass


# Properties to receive via API on update
class CommentUpdate(CommentBase):
    pass


class CommentInDBBase(CommentBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Comment(CommentInDBBase):
    created_at: datetime


# Additional properties stored in DB
class CommentInDB(CommentInDBBase):
    pass
