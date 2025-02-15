import unittest
from bot.bot import TunedFlanBot

class TestTunedFlanBot(unittest.TestCase):
    def setUp(self):
        self.bot = TunedFlanBot()

    def test_get_response(self):
        response = self.bot.get_response("Hello")
        self.assertIsInstance(response, str)
        self.assertNotIn("Error", response)

if __name__ == "__main__":
    unittest.main()