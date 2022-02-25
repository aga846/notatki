import unittest
from testing_examples import is_funny


class MyFileTests(unittest.TestCase):
    def test_is_funny(self):
        self.assertIsNone(is_funny("tim"), "tim should equal None")

    def test_is_funny(self):
        self.assertIsNotNone(is_funny("jonh"), "john should be funny")


if __name__ == "__main__":
    unittest.main()
