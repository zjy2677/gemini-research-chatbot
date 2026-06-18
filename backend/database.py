from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from backend.config import get_database_url


class Base(DeclarativeBase):
    pass


engine = None


def get_engine():
    global engine

    if engine is None:
        engine = create_engine(
            get_database_url(),
            pool_pre_ping=True,
        )

    return engine


def create_tables() -> None:
    from backend.models.users import User

    Base.metadata.create_all(bind=get_engine())
