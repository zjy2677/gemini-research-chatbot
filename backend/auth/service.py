from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.auth.security import hash_password, verify_password
from backend.models.users import User


def find_user_by_username(db: Session, username: str) -> Optional[User]:
    clean_username = username.strip().lower()

    return db.query(User).filter(User.username == clean_username).first()


def find_user_by_email(db: Session, email: str) -> Optional[User]:
    clean_email = email.strip().lower()

    return db.query(User).filter(User.email == clean_email).first()


def register_user(
    db: Session,
    username: str,
    password: str,
    first_name: str,
    last_name: str,
    age: int,
    gender: str,
    email: str,
) -> User:
    clean_username = username.strip().lower()
    clean_email = email.strip().lower()
    clean_first_name = first_name.strip()
    clean_last_name = last_name.strip()
    clean_gender = gender.strip()

    if not clean_username:
        raise ValueError("Username is required.")

    if not password:
        raise ValueError("Password is required.")

    if not clean_first_name:
        raise ValueError("First name is required.")

    if not clean_last_name:
        raise ValueError("Last name is required.")

    if age <= 0:
        raise ValueError("Age must be greater than 0.")

    if not clean_gender:
        raise ValueError("Gender is required.")

    if not clean_email:
        raise ValueError("Email is required.")

    if find_user_by_username(db, clean_username):
        raise ValueError("That username is already registered.")

    if find_user_by_email(db, clean_email):
        raise ValueError("That email is already registered.")

    user = User(
        username=clean_username,
        password_hash=hash_password(password),
        first_name=clean_first_name,
        last_name=clean_last_name,
        age=age,
        gender=clean_gender,
        email=clean_email,
    )

    db.add(user)

    try:
        db.commit()
    except IntegrityError as error:
        db.rollback()
        raise ValueError("Username or email already exists.") from error

    db.refresh(user)

    return user


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = find_user_by_username(db, username)

    if user is None:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user
