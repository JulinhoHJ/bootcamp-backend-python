from db import db
from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    DateTime,
    func,
    ForeignKey
)
from sqlalchemy.orm import relationship

class AreaSede(db.Model):
    __tablename__ = 'areas_sedes'

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    area_id = Column(Integer, ForeignKey('areas.id'), nullable=False)
    sede_id = Column(Integer, ForeignKey('sedes.id'), nullable=False)

    area = relationship('Area')
    sede = relationship('Sede')

    def to_json(self):
        return {
            'id': self.id,
            'area_id': self.area_id,
            'sede_id': self.sede_id
        }
