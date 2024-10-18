import unittest
from words import solutions

class TestMyFile(unittest.TestCase):
    def test_words_solutions(self):
        self.assertEqual(solutions(["good","god"]), 1)
        self.assertEqual(solutions(["car","carpet","torch","run","running"]), 2)
        self.assertEqual(solutions(["good","gtt"]), 1)


if __name__ == "__main__":
    unittest.main()



