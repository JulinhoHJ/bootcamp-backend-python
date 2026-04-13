from pydantic import BaseModel, Field

class LoginSchema(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., min_length=8)