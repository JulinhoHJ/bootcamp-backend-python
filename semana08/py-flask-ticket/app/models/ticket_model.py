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

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(15), nullable=False, unique=True)
    access_key = Column(String(6), nullable=False)
    status = Column(String(20), default='REGISTRADO') # REGISTRADO, ASIGNADO, ATENDIDO, CERRADO
    date_assigned = Column(DateTime)
    date_attention = Column(DateTime)
    solution = Column(Text)
    valoration = Column(Integer)
    date_closed = Column(DateTime)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    ticket_detail_id = Column(Integer, ForeignKey('ticket_details.id'), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    ticket_detail = relationship('TicketDetail')
    user = relationship('User')

    def to_json(self):
        return {
            'id': self.id,
            'code': self.code,
            'access_key': self.access_key,
            'status': self.status,
            'date_assigned': self.date_assigned,
            'date_attention': self.date_attention,
            'solution': self.solution,
            'valoration': self.valoration,
            'date_closed': self.date_closed,
            'user_id': self.user_id,
            'ticket_details': {
                'id': self.ticket_detail.id,
                'applicant': self.ticket_detail.applicant,
                'phone': self.ticket_detail.phone,
                'description': self.ticket_detail.description,
                'area_sede_id': self.ticket_detail.area_sede_id,
                'category_id': self.ticket_detail.category_id
            }
        }