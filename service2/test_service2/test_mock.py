from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestConsole(TestBase):
    def test_playstation4(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_console'))
            self.assertIn(b'Playstation 4', response.data)

class TestConsole(TestBase):
    def test_playstation5(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_console'))
            self.assertIn(b'Playstation 5', response.data)

    def test_pc(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_console'))
            self.assertIn(b'PC', response.data)


    def test_XBOX(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_console'))
            self.assertIn(b'XBOX Series X', response.data)

    def test_nintendo(self):
        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for('get_console'))
            self.assertIn(b'Nintendo Switch', response.data)