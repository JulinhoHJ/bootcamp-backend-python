from app.models.sede_model import Sede
from app.schemas.sede_schema import SedeSchema
from db import db

class SedeService:
    def get_all(self) -> list[Sede]:
        sedes = Sede.query.filter_by(is_active=True).all()
        return sedes
    
    def create(self, data: SedeSchema) -> Sede:
        sede = Sede(
            name=data.name
        )
        db.session.add(sede)
        db.session.commit()
        return sede
    
    def get_by_id(self, id: int) -> Sede | None:
        sede = Sede.query.filter_by(
            id=id, 
            is_active=True
        ).first()
        return sede
    
    def update(self, sede: Sede, data: SedeSchema) -> Sede:
        sede.name = data.name
        db.session.commit()
        return sede
    
    def delete(self, sede: Sede):
        sede.is_active = False
        db.session.commit()
        return sede
    
sede_service = SedeService()