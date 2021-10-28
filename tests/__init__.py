from flask_testing import TestCase
from EnGo import create_app
from EnGo.models import db


class Test(TestCase):

    def create_app(self):
        test_config = dict(
            MONGODB_SETTINGS={"db": "test"},
            TESTING=True
        )
        app = create_app(test_config)

        return app

    def setUp(self):
        self.client = self.app.test_client()
        self.db = db
