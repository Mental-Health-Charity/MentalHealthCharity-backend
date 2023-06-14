from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.helpers.required_role_enum import RequiredRoleEnum
from app.models.article import Article
from app.schemas.article import ArticleCreate, ArticleUpdate


class CRUDArticle(CRUDBase[Article, ArticleCreate, ArticleUpdate]):
    def get_all(self, db: Session):
        return db.query(Article).filter()

    def get_for_volunteers(self, db: Session):
        return db.query(Article).filter(
            or_(
                Article.required_role == RequiredRoleEnum.ANYONE,
                Article.required_role == RequiredRoleEnum.VOLUNTEER,
            )
        )

    def get_for_users(self, db: Session):
        return db.query(Article).filter(
            Article.required_role == RequiredRoleEnum.ANYONE
        )


article = CRUDArticle(Article)
