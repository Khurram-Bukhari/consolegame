from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_console(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "Playstation 4,Call of Duty: Black ops 1"
                p.return_value.text = "Play Call of Duty: Black ops 1 on Playstation 4"
                response = self.client.get(url_for('get_consolegame'))
                self.assertIn(b'Playstation 4,Call of Duty: Black ops 1', response.data)
                self.assertIn(b'Play Call of Duty: Black ops 1 on Playstation 4', response.data)