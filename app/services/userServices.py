from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.repositories.userRepository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserCreate, UserLogin, UserRead
from app.schemas.auth import Token


def register_user(db: Session, user_in: UserCreate) -> UserRead:
    repo = UserRepository(db)

    existing = repo.get_by_email(user_in.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    hashed = hash_password(user_in.password)
    user = repo.create_user(
        email=user_in.email,
        hashed_password=hashed,
        name=user_in.name,
    )

    return UserRead.model_validate(user)


def login_user(db: Session, form_data: OAuth2PasswordRequestForm) -> Token:
    repo = UserRepository(db)

    user = repo.get_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    access_token = create_access_token(subject=user.id)
    return Token(access_token=access_token, token_type="bearer")

