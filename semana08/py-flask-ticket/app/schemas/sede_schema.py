from pydantic import BaseModel, Field

class SedeSchema(BaseModel):
  name: str = Field(..., min_length=3, max_length=100)