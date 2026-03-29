import unittest
from app import get_joke

class TestJokeApp(unittest.TestCase):
    def test_get_joke_returns_string(self):
        """Verify the API returns a non-empty string."""
        result = get_joke()
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == "__main__":
    unittest.main()