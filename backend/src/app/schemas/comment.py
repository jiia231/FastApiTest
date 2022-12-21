from datetime import datetime
from typing import Optional

from pydantic import BaseModel


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
    user_id: Optional[int]
    post_id: Optional[int]
    content: Optional[str]


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
