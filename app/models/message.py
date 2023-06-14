from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class Message(Base):
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    sender = relationship("User")
    creation_date = Column(DateTime, default=func.now(), nullable=False)
    content = Column(String(2048))
    chat_id = Column(Integer, ForeignKey("chat.id"), nullable=False)
