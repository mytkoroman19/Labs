import unittest
import sys
import os

# Додаємо шлях до папки src, щоб Python міг знайти модуль tree_logic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab3 import BinaryTree, invert_binary_tree

class TestInvertBinaryTree(unittest.TestCase):

    def test_standard_tree(self):
        # Створюємо дерево 1 -> (2, 3)
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)

        invert_binary_tree(root)

        # Перевірка
        self.assertEqual(root.left.value, 3)
        self.assertEqual(root.right.value, 2)

    def test_empty_tree(self):
        self.assertIsNone(invert_binary_tree(None))

if __name__ == "__main__":
    unittest.main()