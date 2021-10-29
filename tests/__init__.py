from flask_testing import TestCase
from mongoengine import connect, disconnect
from EnGo import create_app
from EnGo.models import db


class Test(TestCase):

    def create_app(self):
        test_config = dict(
            MONGODB_SETTINGS={
                "db": "test",
                "connect": False
            },
            TESTING=True
        )
        app = create_app(test_config)
        self.client = app.test_client()
        self.db = db

        return app

    def setUp(self):
        disconnect()
        connect('test', host='mongomock://localhost', alias="default")

    def tearDown(self):
        disconnect()
