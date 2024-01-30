import unittest

from flask_testing import TestCase

from muscle_metrics import app


class TestLoginRoute(TestCase):

    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_login_route(self):
        response = self.client.get("/login")
        self.assert200(response)
        self.assert_template_used("login/login.html")

if __name__ == '__main__':
    unittest.main()