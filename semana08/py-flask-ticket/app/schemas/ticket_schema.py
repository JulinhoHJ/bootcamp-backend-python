from pydantic import BaseModel, Field

class TicketDetailSchema(BaseModel):
  applicant: str = Field(...,description='Nombre del solicitante', max_length=100)
  email: str = Field(...,description='Email del solicitante', max_length=100)
  phone: str = Field(description='Telefono del solicitante', max_length=15)
  description: str = Field(...,description='Descripcion del ticket')
  area_sede_id: int = Field(...,description='Id de la area de sede')
  category_id: int = Field(...,description='Id de la categoria')

class TicketSchema(BaseModel):
  ticket_details: TicketDetailSchema