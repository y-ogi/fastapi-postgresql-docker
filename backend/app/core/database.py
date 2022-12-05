import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

db_engine = sa.create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


