from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentUpdate


class CRUDComment(CRUDBase[Comment, CommentCreate, CommentUpdate]):
    def get_by_post_id(self, db: Session, post_id: Any) -> list[Optional[Comment]]:
        return db.query(Comment).filter(post_id == post_id).all()



comment = CRUDComment(Comment)
