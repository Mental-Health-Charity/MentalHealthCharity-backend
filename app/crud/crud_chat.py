from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.chat import Chat
from app.schemas.chat import ChatCreate, ChatUpdate
from app.models.user import User

class CRUDChat(CRUDBase[Chat, ChatCreate, ChatUpdate]):

    def create(self, db: Session,  obj_in: ChatCreate, **kwargs) -> Chat:
        user = kwargs.get("user")
        db_obj = Chat(
            name=obj_in.name,
            created_by_id=user.id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def add_participant(
        self, db: Session, *, chat: Chat, user: Optional[User]
    ) -> Chat:
        chat.participants.append(user)
        db.add(chat)
        db.commit()
        db.refresh(chat)
        return chat

    def remove_participant(
        self, db: Session, *, chat: Chat, user: Optional[User]
    ) -> Chat:
        chat.participants.remove(user)
        db.add(chat)
        db.commit()
        db.refresh(chat)
        return chat


chat = CRUDChat(Chat)
