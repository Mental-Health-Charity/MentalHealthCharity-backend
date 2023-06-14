from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter()


@router.get("/{chat_id}", response_model=Page[schemas.Message])
def get_chat_messages(
    chat_id: int,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_active_user),
) -> Any:
    messages = crud.message.get_chat_messages(db, chat_id=chat_id)
    return paginate(messages)
@router.post("/{chat_id}", response_model=schemas.Message)
def send_message(
    chat_id: int,
    obj_in:schemas.MessageCreate,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve users.
    """
    message = crud.message.create(db, obj_in=obj_in, user=current_user, chat_id=chat_id)
    return message

