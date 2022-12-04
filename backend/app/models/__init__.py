from sqlalchemy import (
    BOOLEAN,
    Column,
    INTEGER,
    TEXT,
    TIMESTAMP,
    VARCHAR,
)
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(
        INTEGER,
        primary_key=True,
        autoincrement=True,
    )

    created_at = Column(
        'created_at',
        TIMESTAMP(timezone=True),
        server_default=current_timestamp(),
        nullable=False,
        comment='created at',
    )

    updated_at = Column(
        'updated_at',
        TIMESTAMP(timezone=True),
        onupdate=current_timestamp(),
        comment='updated at',
    )

class Item(BaseModel):
    __tablename__ = 'items'

    name = Column(TEXT, unique=True, nullable=False)