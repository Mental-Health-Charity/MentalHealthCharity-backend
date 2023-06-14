from datetime import date
from typing import List, Optional

from pydantic import BaseModel

from app.schemas.user import User


# Shared properties
class ChatBase(BaseModel):
    name: Optional[str] = None


# Properties to receive via API on creation
class ChatCreate(ChatBase):
    pass


# Properties to receive via API on update
class ChatUpdate(ChatBase):
    pass


class ChatInDBBase(ChatBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Chat(ChatInDBBase):
    participants: List[User] = []
    is_active: bool = True
    creation_date: date
    # messages


# Additional properties stored in DB
class ChatInDB(ChatInDBBase):
    hashed_password: str
