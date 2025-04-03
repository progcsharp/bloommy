from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, \
    Integer, String, Boolean, Enum, ForeignKey,\
    MetaData
# Pay attentions if you use another DB like Oracle, MySQL etc.
# This types implement for specific dialect
from sqlalchemy.dialects.postgresql import JSONB, FLOAT

from sqlalchemy.orm import relationship

from .utils import conventions


meta = MetaData(naming_convention=conventions)

Base = declarative_base(metadata=meta)


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    nickname = Column(String)

    def __init__(self, tg_id, nickname):
        self.tg_id = tg_id
        self.nickname = nickname

