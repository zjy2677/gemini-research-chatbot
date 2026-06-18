from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from backend.database import get_engine


SessionLocal = None


def get_session_factory():
    global SessionLocal

    if SessionLocal is None:
        SessionLocal = sessionmaker(
            bind=get_engine(),
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    return SessionLocal


@contextmanager
def get_session():
    session_factory = get_session_factory()
    db = session_factory()

    try:
        yield db
    finally:
        db.close()


def get_db():
    session_factory = get_session_factory()
    db = session_factory()

    try:
        yield db
    finally:
        db.close()
