from typing import Optional, List

from app.schemas.user import User
from pydantic import BaseModel
from datetime import datetime


# Shared properties
class MessageBase(BaseModel):
    content: str

# Properties to receive via API on creation
class MessageCreate(MessageBase):
    pass


class MessageInDBBase(MessageBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Message(MessageInDBBase):
    sender: User
    creation_date: datetime


# Additional properties stored in DB
class MessageInDB(MessageInDBBase):
    pass
