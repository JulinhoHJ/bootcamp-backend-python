from app.models.ticket_model import Ticket
from app.schemas.ticket_schema import TicketSchema
from app.models.ticket_detail_model import TicketDetail
from db import db
import secrets
import string
from datetime import datetime

class TicketService:

  def generate_access_key(self, length: int = 6) -> str:
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(length))

  def get_all(self) -> list[Ticket]:
    tickets = Ticket.query.all()
    return tickets
  
  def create(self, data: TicketSchema) -> Ticket:
    
    ticket_detail = TicketDetail(
      applicant=data.ticket_details.applicant,
      email=data.ticket_details.email,
      phone=data.ticket_details.phone,
      description=data.ticket_details.description,
      area_sede_id=data.ticket_details.area_sede_id,
      category_id=data.ticket_details.category_id
    )
    db.session.add(ticket_detail)
    db.session.flush()

    year = datetime.now().year

    last_ticket = Ticket.query.filter(
        Ticket.code.like(f'%-{year}')
    ).order_by(Ticket.id.desc()).first()

    new_number = 1

    if last_ticket:
        last_number = int(last_ticket.code.split('-')[1])
        new_number = last_number + 1

    new_code = f'T-{str(new_number).zfill(6)}-{year}'

    access_key = self.generate_access_key()

    ticket = Ticket(
      code=new_code,
      access_key=access_key,
      ticket_detail_id=ticket_detail.id
    )

    db.session.add(ticket)
    db.session.commit()
    return ticket
  
ticket_service = TicketService()


