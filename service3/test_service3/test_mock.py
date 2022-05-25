from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestGame(TestBase):
    def test_COD(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_game'))
            self.assertIn(b'Call of Duty: Black ops 1', response.data)

class TestConsole(TestBase):
    def test_GodofWar(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_game'))
            self.assertIn(b'God of War: Ragnorak', response.data)

    def test_CSGO(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_game'))
            self.assertIn(b'Counter-Strike: Global Offensive', response.data)


    def test_Halo(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_game'))
            self.assertIn(b'Halo Infinite', response.data)

    def test_mario(self):
        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for('get_game'))
            self.assertIn(b'Mario Kart', response.data)