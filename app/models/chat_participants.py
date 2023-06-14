from sqlalchemy import Column, ForeignKey, Integer

from app.db.base_class import Base


class ChatParticipants(Base):
    chat_id = Column(Integer, ForeignKey("chat.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
