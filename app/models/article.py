from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base
from app.helpers.required_role_enum import RequiredRoleEnum


class Article(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_by_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_by = relationship("User")
    creation_date = Column(DateTime, default=func.now(), nullable=False)
    required_role = Column(
        Enum(RequiredRoleEnum), default=RequiredRoleEnum.ANYONE, nullable=False
    )
    title = Column(String(256), nullable=False)
    content = Column(String(16384), nullable=False)
    banner_url = Column(String(16384), nullable=False)
