from . import Test
from flask import url_for
from EnGo.models.product import Product


class ProductTest(Test):

    def setUp(self):
        Test.setUp(self)
        self.product = Product(
            id=1,
            name='Test Product',
            price=10
        )
        self.product.save()


class TestGetProducts(ProductTest):

    def test_should_return_list_of_all_products_given_get_request(self):
        with self.client as client:
            response = client.get(
                url_for('products')
            )

        self.assertEqual(len(response.json), 1)


class TestGetProduct(ProductTest):

    def test_should_retrive_product_given_get_request_and_valid_product_id(self):
        with self.client as client:
            response = client.get(
                url_for('products', product_id=self.product.id)
            )

        self.assertEqual(response.json['name'], self.product.name)

    def test_should_return_none_values_given_invalid_id(self):
        with self.client as client:
            response = client.get(
                url_for('products', product_id=0)
            )

        self.assertEqual(response.json['name'], None)


class TestAddProduct(ProductTest):

    def test_should_add_product_given_post_request_with_valid_product_data(self):
        product_data = dict(
            id=2,
            name='Test Product 2',
            price=10
        )
        with self.client as client:
            client.post(
                url_for('products'),
                data=product_data
            )

        self.assertTrue(Product.objects(name='Test Product 2').first())


class TestUpdateProduct(ProductTest):

    def test_should_update_product_given_put_request_and_valid_product_data(self):
        product_data = dict(
            name='New Name',
            price=10
        )
        with self.client as client:
            client.put(
                url_for('products', product_id=self.product.id),
                data=product_data
            )

        self.assertEqual(self.product.name, 'New Name')


class TestDeleteProduct(ProductTest):

    def test_should_delete_product_given_valid_product_id(self):
        with self.client as client:
            client.delete(
                url_for('products', product_id=self.product.id)
            )

        self.assertNotIn(self.product, self.db.session)
