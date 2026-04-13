from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func
)
from sqlalchemy.orm import relationship

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())

    users = relationship('User')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }