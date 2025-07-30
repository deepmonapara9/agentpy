import os
import sqlmodel
from sqlmodel import Session, SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set")

# This will create a SQLAlchemy engine for us to use with SQLModel which will help us interact with the database
engine = sqlmodel.create_engine(DATABASE_URL)

# Database models
def init_db():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)

# This will create a session for us to use with SQLModel which will help us interact with the database
def get_session():
    with Session(engine) as session:
        yield session
