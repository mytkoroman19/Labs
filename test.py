import unittest
from lab1 import find_kth_largest

class TestFindKthLargest(unittest.TestCase):
    def test_find_kth_largest(self):
        nums = [4, 10, 5, 12, 3, 17, 1]
        k_value = 2
        expected_value = 12
        expected_position = 3

        value, position = find_kth_largest(nums, k_value)

        self.assertEqual(value, expected_value)
        self.assertEqual(position, expected_position)

    def test_invalid_k(self):
        nums = [4, 10, 5]
        k_value = 0

        with self.assertRaises(ValueError):
            find_kth_largest(nums, k_value)

        k_value = 4

        with self.assertRaises(ValueError):
            find_kth_largest(nums, k_value)

if __name__ == "__main__":
    unittest.main()
