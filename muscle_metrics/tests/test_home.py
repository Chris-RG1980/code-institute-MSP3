import unittest

from flask_testing import TestCase

from muscle_metrics import app


class TestHomeRoute(TestCase):

    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_home_route(self):
        response = self.client.get("/")
        self.assert200(response)
        self.assert_template_used("home/index.html")

if __name__ == '__main__':
    unittest.main()