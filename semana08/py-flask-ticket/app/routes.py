from flask_restful import Api
from app import app
from app.resources.user_resource import (
  UserResource,
  ManageUserResource
)
from app.resources.role_resource import RoleResource
from app.resources.auth_resource import LoginResource
from app.resources.sede_resource import (
  SedeResource,
  ManageSedeResource
)
from app.resources.category_resource import (
  CategoryResource,
  ManageCategoryResource
)
from app.resources.area_resource import (
  AreaResource,
  ManageAreaResource
)
from app.resources.area_sede_resource import (
  AreaSedeResource,
  ManageAreaSedeResource
)
#from app.resources.product_resource import (
#  ProductResource, 
#  ManageProductResource
#)
#from app.resources.sale_resource import SaleResource

api = Api(app, prefix='/api')

api.add_resource(UserResource, '/users')
api.add_resource(ManageUserResource, '/users/<int:id>')
api.add_resource(LoginResource, '/auth/login')
api.add_resource(RoleResource, '/roles')

api.add_resource(SedeResource, '/sedes')
api.add_resource(ManageSedeResource, '/sedes/<int:id>')

api.add_resource(CategoryResource, '/categories')
api.add_resource(ManageCategoryResource, '/categories/<int:id>')

api.add_resource(AreaResource, '/areas')
api.add_resource(ManageAreaResource, '/areas/<int:id>')

api.add_resource(AreaSedeResource, '/areas_sedes')
api.add_resource(ManageAreaSedeResource, '/areas_sedes/<int:id>')
#api.add_resource(ProductResource, '/products')
#api.add_resource(ManageProductResource, '/products/<int:id>')
#api.add_resource(SaleResource, '/sales')