import unittest
from lab4 import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        """Створюємо новий об'єкт черги перед кожним тестом."""
        self.pq = PriorityQueue()

    def test_insert_and_peek(self):
        """Перевірка, що peek завжди бачить найвищий пріоритет."""
        self.pq.insert("low", 10)
        self.pq.insert("high", 100)
        self.pq.insert("mid", 50)
        
        value, priority = self.pq.peek()
        self.assertEqual(value, "high")
        self.assertEqual(priority, 100)

    def test_pop_order(self):
        """Перевірка, що елементи виходять у порядку спадання пріоритету."""
        self.pq.insert("task1", 10)
        self.pq.insert("task2", 30)
        self.pq.insert("task3", 20)
        
    
        self.assertEqual(self.pq.pop(), ("task2", 30))
        self.assertEqual(self.pq.pop(), ("task3", 20))
        self.assertEqual(self.pq.pop(), ("task1", 10))

    def test_same_priority(self):
        """Перевірка обробки однакових пріоритетів."""
        self.pq.insert("first", 50)
        self.pq.insert("second", 50)
        
        
        self.assertEqual(self.pq.pop(), ("second", 50))
        self.assertEqual(self.pq.pop(), ("first", 50))

    def test_empty_queue(self):
        """Перевірка роботи з порожньою чергою."""
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.pop())

    def test_complex_tree(self):
        """Тест на складнішу структуру дерева (видалення вузла з правим піддеревом)."""
       
        self.pq.insert("root", 50)
        self.pq.insert("left", 100)
        self.pq.insert("left_right", 80)
        

        self.assertEqual(self.pq.pop(), ("left", 100))
        
        self.assertEqual(self.pq.peek(), ("left_right", 80))

if __name__ == "__main__":
    unittest.main()