import unittest
import sys
import os

# Додаємо батьківську директорію до sys.path, щоб знайти папку src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab2 import min_eating_speed

class TestJackieBananas(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)

    def test_example_2(self):
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 5), 30)

    def test_example_3(self):
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 6), 23)

    def test_large_h(self):
        self.assertEqual(min_eating_speed([10, 10, 10], 100), 1)

if __name__ == '__main__':
    unittest.main()