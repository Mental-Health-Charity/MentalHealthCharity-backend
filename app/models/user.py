from sqlalchemy import Boolean, Column, Enum, Integer, String

from app.db.base_class import Base
from app.helpers.user_enum import UserRoleEnum


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(32), index=True)
    email = Column(String(32), unique=True, index=True, nullable=False)
    hashed_password = Column(String(254), nullable=False)
    is_active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER, nullable=False)
