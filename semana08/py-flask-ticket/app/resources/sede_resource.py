from flask_restful import Resource
from flask import request
from app.services.sede_service import sede_service
from pydantic import ValidationError
from app.schemas.sede_schema import SedeSchema
from flask_jwt_extended import jwt_required

class SedeResource(Resource):
  def get(self):
    try:
      sedes = sede_service.get_all()
      sedes_list = []
      for sede in sedes:
        sedes_list.append(
          sede.to_json()
        )
      return sedes_list, 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400

  def post(self):
    try:
      json = request.get_json()
      validated_data = SedeSchema.model_validate(json)
      sede = sede_service.create(validated_data)
      return sede.to_json(), 200
    except ValidationError as e:
      return {
        'error': e.errors()
      }, 400
    except Exception as e:
      return {
        'error': str(e)
      }, 400

class ManageSedeResource(Resource):
  def get(self, id: int):
    try:
      sede = sede_service.get_by_id(id)

      if not sede:
        return {
          'error': 'Sede not found'
        }, 404

      return sede.to_json(), 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400

  def put(self, id: int):
    try:
      json = request.get_json()
      validated_data = SedeSchema.model_validate(json)
      sede = sede_service.get_by_id(id)

      if not sede:
        return {
          'error': 'Sede not found'
        }, 404
      
      sede = sede_service.update(sede, validated_data)
      return sede.to_json(), 200
    except ValidationError as e:
      return {
        'error': e.errors()
      }, 400
    except Exception as e:
      return {
        'error': str(e)
      }, 400

  @jwt_required()
  def delete(self, id: int):
    try:
      sede = sede_service.get_by_id(id)

      if not sede:
        return {
          'error': 'Sede not found'
        }, 404
      
      sede_service.delete(sede)
      return None, 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400