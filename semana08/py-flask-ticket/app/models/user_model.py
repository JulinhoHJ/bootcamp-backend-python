from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    func,
    ForeignKey
)
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    sede_id = Column(Integer, ForeignKey('sedes.id'), nullable=False)

    role = relationship('Role', back_populates='users')
    sede = relationship('Sede')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'role_id': self.role_id,
            'sede_id': self.sede_id
        }
