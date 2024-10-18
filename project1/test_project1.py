import unittest
from words import solutions

class TestMyFile(unittest.TestCase):
    def test_words_solutions(self):
        self.assertEqual(solutions(["good","god"]), 1)
        self.assertEqual(solutions(["car","carpet","torch","run","runn"]), 1)
        self.assertEqual(solutions(["good","gtt"]), 0)


if __name__ == "__main__":
    unittest.main()
    print("Done")



