from sqlalchemy.orm import Session

from app.database.models import User


def get_user(db: Session, session_id: str):
    return (
        db.query(User)
        .filter(User.session_id == session_id)
        .first()
    )


def create_user(db: Session, session_id: str):
    user = User(session_id=session_id)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def update_language(db, session_id: str, language: str):
    user = get_user(db, session_id)

    if user:
        user.language = language
        db.commit()
        db.refresh(user)

    return user


def update_name(db, session_id: str, name: str):
    user = get_user(db, session_id)

    if user:
        user.name = name
        db.commit()
        db.refresh(user)

    return user