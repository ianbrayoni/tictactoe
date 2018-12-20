from unittest import TestCase
from api import api


class TicTacToeApiTestCase(TestCase):
    def setUp(self):
        api.app.config["TESTING"] = True
        self.api = api.app.test_client()

    def tearDown(self):
        api.app.config["TESTING"] = False

    def test_valid_request(self):
        response = self.api.get("/tictactoe?board=+xxo++o++")
        self.assertEqual(response.status, "200 OK")
        assert b"oxxo  o  " in response.data

    def test_invalid_request(self):
        response = self.api.get("/tictactoe?board=askdhf")
        self.assertEqual(response.status, "400 BAD REQUEST")
