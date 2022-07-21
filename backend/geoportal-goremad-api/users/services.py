from sqlalchemy.orm import Session

from users.models import User


def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).where(User.username == username, User.status).first()
