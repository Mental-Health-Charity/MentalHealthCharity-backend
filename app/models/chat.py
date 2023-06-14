from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class Chat(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    participants = relationship("User", secondary="chatparticipants")
    is_active = Column(Boolean, default=True, nullable=False)
    creation_date = Column(Date, default=func.now(), nullable=False)
    created_by_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_by = relationship("User", foreign_keys=[created_by_id])
    messages = relationship("Message")
