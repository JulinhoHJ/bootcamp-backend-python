from flask_restful import Resource
from flask import request
from app.services.area_service import area_service
from pydantic import ValidationError
from app.schemas.area_schema import AreaSchema
from flask_jwt_extended import jwt_required

class AreaResource(Resource):
  def get(self):
    try:
      areas = area_service.get_all()
      areas_list = []
      for area in areas:
        areas_list.append(
          area.to_json()
        )
      return areas_list, 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400

  def post(self):
    try:
      json = request.get_json()
      validated_data = AreaSchema.model_validate(json)
      area = area_service.create(validated_data)
      return area.to_json(), 200
    except ValidationError as e:
      return {
        'error': e.errors()
      }, 400
    except Exception as e:
      return {
        'error': str(e)
      }, 400

class ManageAreaResource(Resource):
  def get(self, id: int):
    try:
      area = area_service.get_by_id(id)

      if not area:
        return {
          'error': 'Area not found'
        }, 404

      return area.to_json(), 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400

  def put(self, id: int):
    try:
      json = request.get_json()
      validated_data = AreaSchema.model_validate(json)
      area = area_service.get_by_id(id)

      if not area:
        return {
          'error': 'Area not found'
        }, 404
      
      area = area_service.update(area, validated_data)
      return area.to_json(), 200
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
      area = area_service.get_by_id(id)

      if not area:
        return {
          'error': 'Area not found'
        }, 404
      
      area_service.delete(area)
      return None, 200
    except Exception as e:
      return {
        'error': str(e)
      }, 400