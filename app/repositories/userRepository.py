from typing import Optional

from sqlalchemy.orm import Session

from app.models.users import User


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.get(User, user_id)

    def create_user(
        self,
        *,
        email: str,
        hashed_password: str,
        name: Optional[str] = None,
        role: str = "user",
    ) -> User:
        user = User(
            email=email,
            password=hashed_password,
            name=name,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

