from flask_restful import Resource
from flask import request
from app.schemas.ticket_schema import TicketSchema
from app.services.ticket_service import ticket_service
from pydantic import ValidationError
from flask_jwt_extended import jwt_required
from db import db

class TicketResource(Resource):
  @jwt_required()
  def get(self):
    try:
      tickets = ticket_service.get_all()
      tickets_list = []
      for ticket in tickets:
        tickets_list.append(ticket.to_json())
      
      return tickets_list, 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400

  def post(self):
    try:
      json = request.get_json()
      validated_data = TicketSchema.model_validate(json)
      ticket = ticket_service.create(validated_data)
      return ticket.to_json(), 200
    except ValidationError as e:
      return {
        'error': e.errors()
      }, 400
    except Exception as e:
      db.session.rollback()
      return {
        'error': str(e)
      }, 400