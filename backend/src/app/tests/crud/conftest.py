import pytest
from app import crud
from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostCreate, PostUpdate
from app.schemas.user import UserCreate, UserUpdate
from app.tests.utils.utils import random_email, random_lower_string
from sqlalchemy.orm import Session


@pytest.fixture(scope="function")
def user(db: Session) -> User:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)
    yield user


@pytest.fixture(scope="function")
def post(db: Session) -> Post:
    title = random_lower_string()
    content = random_lower_string()
    post_in = PostCreate(title=title, content=content)
    post = crud.post.create(db, obj_in=post_in)
    yield post
