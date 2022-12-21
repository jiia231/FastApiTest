from app import crud
from app.schemas.post import PostCreate, PostUpdate
from app.tests.utils.utils import random_lower_string
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def test_create_post(db: Session) -> None:
    title = random_lower_string()
    content = random_lower_string()
    post_in = PostCreate(title=title, content=content)
    post = crud.post.create(db, obj_in=post_in)
    assert post
    assert post.title == title
    assert post.content == content


def test_get_post(db: Session) -> None:
    title = random_lower_string()
    content = random_lower_string()
    post_in = PostCreate(title=title, content=content)
    post = crud.post.create(db, obj_in=post_in)
    post_2 = crud.post.get(db, id=post.id)
    assert post_2
    assert jsonable_encoder(post) == jsonable_encoder(post_2)


def test_update_post(db: Session) -> None:
    title = random_lower_string()
    content = random_lower_string()
    post_in = PostCreate(title=title, content=content)
    post = crud.post.create(db, obj_in=post_in)
    new_title = random_lower_string()
    post_in_update = PostUpdate(title=new_title)
    crud.post.update(db, db_obj=post, obj_in=post_in_update)
    post_2 = crud.post.get(db, id=post.id)
    assert post_2
    assert post.content == post_2.content
    assert new_title == post_2.title
