from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.message import Message
from app.schemas.message import MessageCreate
from app.models.user import User

class CRUDMessage(CRUDBase[Message, MessageCreate, None]):

    def create(self, db: Session,  obj_in: MessageCreate, **kwargs) -> Message:
        user = kwargs.get("user")
        chat_id = kwargs.get("chat_id")
        db_obj = Message(
            content=obj_in.content,
            chat_id=chat_id,
            sender_id=user.id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def get_chat_messages(
        self, db: Session, *, chat_id: int
    ) :
        messages = (
            db.query(Message)
            .filter(
                    Message.chat_id == chat_id,
            ).order_by(Message.creation_date.desc())
        )
        return messages


message = CRUDMessage(Message)
