from app.models.area_sede_model import AreaSede
from app.schemas.area_sede_schema import AreaSedeSchema
from db import db

class AreaSedeService:
    def get_all(self) -> list[AreaSede]:
        areas_sedes = AreaSede.query.filter_by(is_active=True).all()
        return areas_sedes
    
    def create(self, data: AreaSedeSchema) -> AreaSede:
        area_sede = AreaSede(
            area_id=data.area_id,
            sede_id=data.sede_id
        )
        db.session.add(area_sede)
        db.session.commit()
        return area_sede
    
    def get_by_id(self, id: int) -> AreaSede | None:
        area_sede = AreaSede.query.filter_by(
            id=id, 
            is_active=True
        ).first()
        return area_sede
    
    def update(self, area_sede: AreaSede, data: AreaSedeSchema) -> AreaSede:
        area_sede.area_id = data.area_id
        area_sede.sede_id = data.sede_id
        db.session.commit()
        return area_sede
    
    def delete(self, area_sede: AreaSede):
        area_sede.is_active = False
        db.session.commit()
        return area_sede
    
area_sede_service = AreaSedeService()