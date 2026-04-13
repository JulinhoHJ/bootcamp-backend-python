from flask_restful import Resource
from flask import request
from app.services.area_sede_service import area_sede_service
from pydantic import ValidationError
from app.schemas.area_sede_schema import AreaSedeSchema

class AreaSedeResource(Resource):
  def get(self):
    try:
      areas_sedes = area_sede_service.get_all()
      areas_sedes_list = []
      for area_sede in areas_sedes:
        areas_sedes_list.append(
          area_sede.to_json()
        )
      return areas_sedes_list, 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400

  def post(self):
    try:
      json = request.get_json()
      validated_data = AreaSedeSchema.model_validate(json)
      area_sede = area_sede_service.create(validated_data)
      return area_sede.to_json(), 200
    except ValidationError as e:
      return {
        'error': e.errors()
      }, 400
    except Exception as e:
      return {
        'error': str(e)
      }, 400

class ManageAreaSedeResource(Resource):
  def get(self, id: int):
    try:
      area_sede = area_sede_service.get_by_id(id)

      if not area_sede:
        return {
          'error': 'Area de sede not found'
        }, 404

      return area_sede.to_json(), 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400

  def put(self, id: int):
    try:
      json = request.get_json()
      validated_data = AreaSedeSchema.model_validate(json)
      area_sede = area_sede_service.get_by_id(id)

      if not area_sede:
        return {
          'error': 'Area de sede not found'
        }, 404
      
      area_sede = area_sede_service.update(area_sede, validated_data)
      return area_sede.to_json(), 200
    except ValidationError as e:
      return {
        'error': e.errors()
      }, 400
    except Exception as e:
      return {
        'error': str(e)
      }, 400

  def delete(self, id: int):
    try:
      area_sede = area_sede_service.get_by_id(id)

      if not area_sede:
        return {
          'error': 'Area de sede not found'
        }, 404
      
      area_sede_service.delete(area_sede)
      return None, 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400