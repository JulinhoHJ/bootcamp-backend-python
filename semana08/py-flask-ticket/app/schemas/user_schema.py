from pydantic import BaseModel, Field
from typing import Optional

class BaseUserSchema(BaseModel):
    name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    phone: str = Field(..., max_length=15)
    email: str = Field(..., max_length=100)
    role_id: int = Field(..., gt=0)
    sede_id: int = Field(..., gt=0)

class CreateUserSchema(BaseUserSchema):
    password: str = Field(..., min_length=8)

class UpdateUserSchema(BaseUserSchema):
    password: Optional[str] = None

