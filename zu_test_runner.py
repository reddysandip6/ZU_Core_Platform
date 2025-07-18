import unittest
from C_Token_Reputation_Engine.token_engine import TokenEngine
from B_Core_Protocol.core_protocol import ZUCore

class TestZUPlatform(unittest.TestCase):
    def setUp(self):
        self.token_engine = TokenEngine()
        self.zu_core = ZUCore(self.token_engine)

    def test_token_creation(self):
        token = self.token_engine.create_token("user_001", "initial_reputation")
        self.assertIn("token_id", token)
        self.assertEqual(token["reputation"], "initial_reputation")

    def test_reputation_update(self):
        token = self.token_engine.create_token("user_002", 5)
        updated = self.token_engine.update_reputation(token["token_id"], 10)
        self.assertTrue(updated)
        self.assertEqual(self.token_engine.tokens[token["token_id"]]["reputation"], 10)

    def test_access_validation(self):
        token = self.token_engine.create_token("user_003", 7)
        result = self.zu_core.validate_access(token["token_id"])
        self.assertIn("access_granted", result)

if __name__ == "__main__":
    unittest.main()
