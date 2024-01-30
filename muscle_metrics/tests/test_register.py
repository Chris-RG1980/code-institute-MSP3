import unittest

from flask_testing import TestCase

from muscle_metrics import app


class TestRegisterRoute(TestCase):

    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_register_route(self):
        response = self.client.get("/register")
        self.assert200(response)
        self.assert_template_used("register/register.html")

if __name__ == '__main__':
    unittest.main()