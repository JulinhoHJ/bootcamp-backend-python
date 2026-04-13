from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship

class TicketDetail(db.Model):
    __tablename__ = 'ticket_details'

    id = Column(Integer, primary_key=True, index=True)
    applicant = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(15))
    description = Column(Text, nullable=False)
    area_sede_id = Column(Integer, ForeignKey('areas_sedes.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    area_sede = relationship('areas_sedes')
    category = relationship('categories')

    def to_json(self):
        return {
            'id': self.id,
            'applicant': self.applicant,
            'email': self.email,
            'phone': self.phone,
            'description': self.description,
            'area_sede_id': self.area_sede_id,
            'category_id': self.category_id
        }