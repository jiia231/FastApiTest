from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Post])
def read_posts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve posts.
    """
    posts = crud.post.get_multi(db, skip=skip, limit=limit)
    return posts


@router.post("/", response_model=schemas.Post)
def create_post(
    *,
    db: Session = Depends(deps.get_db),
    post_in: schemas.PostCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new post.
    """
    post = crud.post.create(db, obj_in=post_in)
    return post


@router.get("/{post_id}", response_model=schemas.Post)
def read_post_by_id(
    post_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific post by id.
    """
    post = crud.user.get(db, id=post_id)

    return post


@router.get("/{post_id}/comments", response_model=list[schemas.Comment])
def read_post_comments(
    post_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get comments for post by post id.
    """
    comments = crud.comment.get_by_post_id(db, post_id=post_id)

    return comments


@router.post("/{post_id}/comments", response_model=schemas.Comment)
def create_comment(
    comment: schemas.CommentCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create comment for post.
    """
    comment = crud.comment.create(db, obj_in=comment)

    return comment
