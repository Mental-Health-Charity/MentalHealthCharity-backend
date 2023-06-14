from typing import Any, Optional

from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.helpers.user_enum import UserRoleEnum

router = APIRouter()


@router.get("/", response_model=Page[schemas.Article])
def read_articles(
    db: Session = Depends(deps.get_db),
    current_user: Optional[models.User] = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve articles.
    """
    if current_user is None:
        articles = crud.article.get_for_users(db)
        return paginate(articles)
    if current_user.user_role == UserRoleEnum.ADMIN:
        articles = crud.article.get_all(db)
    elif current_user.user_role == UserRoleEnum.VOLUNTEER:
        articles = crud.article.get_for_volunteers(db)
    else:
        articles = crud.article.get_for_users(db)
    return paginate(articles)


@router.get("/public", response_model=Page[schemas.Article])
def read_public_articles(db: Session = Depends(deps.get_db)) -> Any:
    """
    Retrieve articles.
    """
    articles = crud.article.get_for_users(db)
    return paginate(articles)


@router.post(
    "/",
    response_model=schemas.Article,
)
def create_article(
    *,
    db: Session = Depends(deps.get_db),
    article_in: schemas.ArticleCreate,
    current_user=Depends(deps.get_current_active_admin_user),
) -> Any:
    """
    Create new user.
    """
    article = crud.article.create(db, obj_in=article_in, user=current_user)

    return article
