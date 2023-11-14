import datetime
import unittest
from app import create_app


# test db
# test config

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(test_config)
        self.client = self.app.test_client(self)
        with self.app.app_context():
            db.init_app(self.app)
            db.create_all()

    def test_hello_world(self):
        """TEST HELLO"""
        hello_response = self.client.get("/hello/hello")
        hello_json = hello_response.json["message"]
        self.assertEqual(hello_json, "hello, has reached it's target.")            