from pydantic import BaseModel, Field

class AreaSedeSchema(BaseModel):
  area_id: int = Field(..., gt=0)
  sede_id: int = Field(..., gt=0)