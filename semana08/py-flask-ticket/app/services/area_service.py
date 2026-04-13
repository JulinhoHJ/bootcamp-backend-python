from app.models.area_model import Area
from app.schemas.area_schema import AreaSchema
from db import db

class AreaService:
    def get_all(self) -> list[Area]:
        areas = Area.query.filter_by(is_active=True).all()
        return areas
    
    def create(self, data: AreaSchema) -> Area:
        area = Area(
            name=data.name
        )
        db.session.add(area)
        db.session.commit()
        return area
    
    def get_by_id(self, id: int) -> Area | None:
        area = Area.query.filter_by(
            id=id, 
            is_active=True
        ).first()
        return area
    
    def update(self, area: Area, data: AreaSchema) -> Area:
        area.name = data.name
        db.session.commit()
        return area
    
    def delete(self, area: Area):
        area.is_active = False
        db.session.commit()
        return area
    
area_service = AreaService()