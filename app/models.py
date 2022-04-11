from sqlite3 import Timestamp
from unittest.util import _MAX_LENGTH
from sqlalchemy import Column, Integer, String ,Boolean
from sqlalchemy.sql.expression import null, text
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable = False, autoincrement=True)
    username = Column(String, nullable = False, unique=True)
    user_type = Column(String, nullable = False)
    password = Column(String, nullable = False)
    email = Column(String, nullable = False, unique=True)
    mobile = Column(Integer, nullable = False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default = text('now()'))