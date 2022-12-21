from app import crud
from app.models.post import Post
from app.models.user import User
from app.schemas.comment import CommentCreate, CommentUpdate
from app.schemas.post import PostCreate, PostUpdate
from app.schemas.user import UserCreate, UserUpdate
from app.tests.utils.utils import random_email, random_lower_string
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def test_create_comment(db: Session, user: User, post: Post) -> None:
    content = random_lower_string()
    comment_in = CommentCreate(user_id=user.id, post_id=post.id, content=content)
    comment = crud.comment.create(db, obj_in=comment_in)
    assert comment
    assert comment.content == content


def test_get_comment(db: Session, user: User, post: Post) -> None:
    content = random_lower_string()
    comment_in = CommentCreate(user_id=user.id, post_id=post.id, content=content)
    comment = crud.comment.create(db, obj_in=comment_in)
    comment_2 = crud.comment.get(db, id=comment.id)
    assert comment_2
    assert jsonable_encoder(comment) == jsonable_encoder(comment_2)


def test_update_comment(db: Session, user: User, post: Post) -> None:
    content = random_lower_string()
    comment_in = CommentCreate(user_id=user.id, post_id=post.id, content=content)
    comment = crud.comment.create(db, obj_in=comment_in)

    new_content = random_lower_string()
    comment_in_update = CommentUpdate(content=new_content)
    crud.comment.update(db, db_obj=comment, obj_in=comment_in_update)
    comment_2 = crud.comment.get(db, id=comment.id)
    assert comment_2
    assert new_content == comment.content == comment_2.content
