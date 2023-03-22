import os
import secrets
import sys
from typing import Any, Dict, List, Optional, Union

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = "localhost"
    SERVER_HOST: AnyHttpUrl = "http://localhost"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "mentalhealth"
    MYSQL_CONNECTOR: str = os.environ["DATABASE_CONNECTOR"]
    MYSQL_SERVER: str = os.environ["DATABASE_ADDRESS"]
    MYSQL_USER: str = os.environ["DATABASE_USER"]
    MYSQL_PASSWORD: str = os.environ["DATABASE_PASSWORD"]
    MYSQL_DB: str = os.environ["DATABASE_DB"]
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ["DATABASE_URL"]

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return "{}://{}:{}@{}:3306/{}".format(
            values.get("MYSQL_CONNECTOR"),
            values.get("MYSQL_USER"),
            values.get("MYSQL_PASSWORD"),
            values.get("MYSQL_SERVER"),
            values.get("MYSQL_DB"),
        )

    FIRST_SUPERUSER: EmailStr = os.environ["SUPERUSER_EMAIL"]
    FIRST_SUPERUSER_PASSWORD: str = os.environ["SUPERUSER_PASSWORD"]
    USERS_OPEN_REGISTRATION: bool = True

    class Config:
        case_sensitive = True


settings = Settings()
