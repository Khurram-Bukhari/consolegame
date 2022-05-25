from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_ps4_cod(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 4,Call of Duty: Black ops 1')
        self.assertIn(b'Play Call of Duty: Black ops 1 on Playstation 4', response.data)

    def test_ps4_gow(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 4,God of War: Ragnorak')
        self.assertIn(b'Play God of War: Ragnorak on Playstation 4', response.data)

    def test_ps4_csgo(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 4,Counter-Strike: Global Offensive')
        self.assertIn(b'Play Counter-Strike: Global Offensive on Playstation 4', response.data)

    def test_ps4_hi(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 4,Halo Infinite')
        self.assertIn(b'Play Halo Infinite on Playstation 4', response.data)

    def test_ps4_mariokart(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 4,Mario Kart')
        self.assertIn(b'Play Mario Kart on Playstation 4', response.data)

    def test_ps5_cod(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 5,Call of Duty: Black ops 1')
        self.assertIn(b'Play Call of Duty: Black ops 1 on Playstation 5', response.data)

    def test_ps5_gow(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 5,God of War: Ragnorak')
        self.assertIn(b'Play God of War: Ragnorak on Playstation 5', response.data)

    def test_ps5_csgo(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 5,Counter-Strike: Global Offensive')
        self.assertIn(b'Play Counter-Strike: Global Offensive on Playstation 5', response.data)

    def test_ps5_hi(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 5,Halo Infinite')
        self.assertIn(b'Play Halo Infinite on Playstation 5', response.data)

    def test_ps5_mariokart(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Playstation 5,Mario Kart')
        self.assertIn(b'Play Mario Kart on Playstation 5', response.data)

    def test_pc_cod(self):
        response = self.client.post(url_for('console_game_combined'), data = 'PC,Call of Duty: Black ops 1')
        self.assertIn(b'Play Call of Duty: Black ops 1 on PC', response.data)

    def test_pc_gow(self):
        response = self.client.post(url_for('console_game_combined'), data = 'PC,God of War: Ragnorak')
        self.assertIn(b'Play God of War: Ragnorak on PC', response.data)

    def test_pc_csgo(self):
        response = self.client.post(url_for('console_game_combined'), data = 'PC,Counter-Strike: Global Offensive')
        self.assertIn(b'Play Counter-Strike: Global Offensive on PC', response.data)

    def test_pc_hi(self):
        response = self.client.post(url_for('console_game_combined'), data = 'PC,Halo Infinite')
        self.assertIn(b'Play Halo Infinite on PC', response.data)

    def test_pc_mariokart(self):
        response = self.client.post(url_for('console_game_combined'), data = 'PC,Mario Kart')
        self.assertIn(b'Play Mario Kart on PC', response.data)

    def test_xbox_cod(self):
        response = self.client.post(url_for('console_game_combined'), data = 'XBOX Series X,Call of Duty: Black ops 1')
        self.assertIn(b'Play Call of Duty: Black ops 1 on XBOX Series X', response.data)

    def test_xbox_gow(self):
        response = self.client.post(url_for('console_game_combined'), data = 'XBOX Series X,God of War: Ragnorak')
        self.assertIn(b'Play God of War: Ragnorak on XBOX Series X', response.data)

    def test_xbox_csgo(self):
        response = self.client.post(url_for('console_game_combined'), data = 'XBOX Series X,Counter-Strike: Global Offensive')
        self.assertIn(b'Play Counter-Strike: Global Offensive on XBOX Series X', response.data)

    def test_xbox_hi(self):
        response = self.client.post(url_for('console_game_combined'), data = 'XBOX Series X,Halo Infinite')
        self.assertIn(b'Play Halo Infinite on XBOX Series X', response.data)

    def test_xbox_mariokart(self):
        response = self.client.post(url_for('console_game_combined'), data = 'XBOX Series X,Mario Kart')
        self.assertIn(b'Play Mario Kart on XBOX Series X', response.data)

    def test_nintendo_cod(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Nintendo Switch,Call of Duty: Black ops 1')
        self.assertIn(b'Play Call of Duty: Black ops 1 on Nintendo Switch', response.data)

    def test_nintendo_gow(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Nintendo Switch,God of War: Ragnorak')
        self.assertIn(b'Play God of War: Ragnorak on Nintendo Switch', response.data)

    def test_nintendo_csgo(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Nintendo Switch,Counter-Strike: Global Offensive')
        self.assertIn(b'Play Counter-Strike: Global Offensive on Nintendo Switch', response.data)

    def test_nintendo_hi(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Nintendo Switch,Halo Infinite')
        self.assertIn(b'Play Halo Infinite on Nintendo Switch', response.data)

    def test_nintendo_mariokart(self):
        response = self.client.post(url_for('console_game_combined'), data = 'Nintendo Switch,Mario Kart')
        self.assertIn(b'Play Mario Kart on Nintendo Switch', response.data)



