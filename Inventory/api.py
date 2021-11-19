from flask_restful import Api
from .resources import ProductResource

api = Api(prefix='/inventory')

api.add_resource(
    ProductResource,
    '/products',
    '/products/<int:product_id>',
    endpoint='products'
)