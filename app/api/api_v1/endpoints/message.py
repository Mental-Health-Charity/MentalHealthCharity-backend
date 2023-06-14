from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/{chat_id}", response_model=Page[schemas.Message])
def get_chat_messages(
    chat_id: int,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_active_user),
) -> Any:
    chats = crud.chat.get_my(db, user=current_user)
    for chat in chats:
        if chat.id == chat_id:
            messages = crud.message.get_chat_messages(db, chat_id=chat_id)
            return paginate(messages)
    raise HTTPException(
        status_code=300, detail="You can't read messages from this chat"
    )


@router.post("/{chat_id}", response_model=schemas.Message)
def send_message(
    chat_id: int,
    obj_in: schemas.MessageCreate,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve users.
    """
    chats = crud.chat.get_my(db, user=current_user)
    for chat in chats:
        if chat.id == chat_id:
            message = crud.message.create(
                db, obj_in=obj_in, user=current_user, chat_id=chat_id
            )
            return message
    raise HTTPException(status_code=300, detail="You can't send message to this chat")
