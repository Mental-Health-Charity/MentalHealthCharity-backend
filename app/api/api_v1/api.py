from fastapi import APIRouter

from .endpoints import article, chat, login, message, users

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(message.router, prefix="/message", tags=["message"])
api_router.include_router(article.router, prefix="/article", tags=["article"])
