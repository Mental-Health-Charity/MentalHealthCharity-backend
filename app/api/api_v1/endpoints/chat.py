from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.helpers.user_enum import UserRoleEnum

router = APIRouter()


@router.get("/", response_model=Page[schemas.Chat])
def read_chats(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve users.
    """
    if current_user.user_role == UserRoleEnum.ADMIN:
        chats = crud.chat.get_multi(db)
    else:
        chats = crud.chat.get_my(db, user=current_user)
    return paginate(chats)


@router.post(
    "/",
    response_model=schemas.Chat,
)
def create_chat(
    *,
    db: Session = Depends(deps.get_db),
    chat_in: schemas.ChatCreate,
    current_user=Depends(deps.get_current_active_admin_user),
) -> Any:
    """
    Create new user.
    """
    chat = crud.chat.create(db, obj_in=chat_in, user=current_user)

    return chat


@router.post(
    "/{chat_id}/participant/{participant_id}}",
    response_model=schemas.Chat,
    dependencies=[Depends(deps.get_current_active_admin_user)],
)
def add_participant(
    *,
    db: Session = Depends(deps.get_db),
    chat_id: int,
    participant_id: int,
) -> Any:
    """
    Add new participant to chat.
    """
    chat = crud.chat.get(db, id=chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Bad chat")

    participant = crud.user.get(db, id=participant_id)
    if not participant:
        raise HTTPException(status_code=404, detail="Bad user")
    chat = crud.chat.add_participant(db, chat=chat, user=participant)

    return chat


@router.delete(
    "/{chat_id}/corrector/{participant_id}",
    response_model=schemas.Chat,
    dependencies=[Depends(deps.get_current_active_admin_user)],
)
def remove_participant(
    *,
    db: Session = Depends(deps.get_db),
    chat_id: int,
    participant_id: int,
) -> Any:
    """
    Delete participant from chat.
    """
    chat = crud.chat.get(db, id=chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Bad chat")

    participant = crud.user.get(db, id=participant_id)
    if not participant:
        raise HTTPException(status_code=404, detail="Bad user")
    chat = crud.chat.remove_participant(db, chat=chat, user=participant)

    return chat
