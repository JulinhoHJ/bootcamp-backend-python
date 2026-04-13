from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Boolean
)

class Area(db.Model):
    __tablename__ = 'areas'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }