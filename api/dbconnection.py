from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    sqlalchemy_database_url = os.getenv("DATABASE_URL")
    database_service = os.getenv("DATABASE_SERVICE").lower()
    if  database_service == "sqlite":
        return create_engine(
            sqlalchemy_database_url, connect_args={"check_same_thread": False}
        )
    return create_engine(
        sqlalchemy_database_url
    )

engine = get_engine()

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

def get_db():
    db = SessionLocal()
    try:
        if os.getenv("DATABASE_SERVICE").lower() == "sqlite":
            db.execute(text("PRAGMA foreign_keys=ON"))
        yield db
    finally:
        db.close()
