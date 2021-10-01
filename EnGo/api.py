from flask_restful import Api

api = Api(prefix='/inventory')

from .resources import ProductResource
api.add_resource(
    ProductResource,
    '/products',
    '/products/<int:product_id>',
    endpoint='products'
)