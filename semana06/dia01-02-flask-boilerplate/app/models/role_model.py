from db import db
from sqlalchemy import ( # type: ignore
    Column,
    Integer,
    String
)
from sqlalchemy.orm import relationship # type: ignore

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

    users = relationship('User')