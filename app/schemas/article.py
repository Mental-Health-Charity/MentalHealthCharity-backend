from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.helpers.required_role_enum import RequiredRoleEnum
from app.schemas.user import User


# Shared properties
class ArticleBase(BaseModel):
    title: str
    content: str
    banner_url: str


# Properties to receive via API on creation
class ArticleCreate(ArticleBase):
    required_role: RequiredRoleEnum = RequiredRoleEnum.ANYONE


class ArticleUpdate(ArticleBase):
    pass


class ArticleInDBBase(ArticleBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Article(ArticleInDBBase):
    created_by: User
    creation_date: datetime


# Additional properties stored in DB
class ArticleInDB(ArticleInDBBase):
    pass
