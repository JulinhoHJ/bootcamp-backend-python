from pydantic import BaseModel, Field

class AreaSchema(BaseModel):
  name: str = Field(..., min_length=3, max_length=100)