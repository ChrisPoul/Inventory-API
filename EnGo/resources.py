from flask import request
from flask_restful import Resource, marshal_with, fields
from .models.product import Product

product_fields = dict(
    id=fields.Integer,
    name=fields.String,
    price=fields.Integer
)


class ProductResource(Resource):

    @marshal_with(product_fields)
    def get(self, product_id=None):
        if product_id is None:
            return Product.query.all()

        return Product.query.get(product_id)

    def post(self):
        product = Product(
            name=request.form['name'],
            price=request.form['price']
        )
        product.add()

    def put(self, product_id):
        product = Product.query.get(product_id)
        product.update(request.form)

    def delete(self, product_id):
        product = Product.query.get(product_id)
        product.delete()
