from shared.database import SessionLocal


def get_database_context():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
