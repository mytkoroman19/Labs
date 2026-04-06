class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        """Вставка елемента з урахуванням пріоритету."""
        new_node = Node(value, priority)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
       
        if new_node.priority >= current.priority:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
    
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def peek(self):
        """Перегляд елемента з найвищим пріоритетом (найлівіший вузол)."""
        if self.root is None:
            return None
        
        current = self.root
        while current.left is not None:
            current = current.left
        return (current.value, current.priority)

    def pop(self):
        """Видалення та повернення елемента з найвищим пріоритетом."""
        if self.root is None:
            return None

       
        if self.root.left is None:
            highest_node = self.root
            self.root = self.root.right 
            return (highest_node.value, highest_node.priority)

       
        parent = self.root
        current = self.root.left
        while current.left is not None:
            parent = current
            current = current.left

      
        highest_node = current
       
        parent.left = current.right
        
        return (highest_node.value, highest_node.priority)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("Завдання низької важливості", 10)
    pq.insert("Критична помилка", 100)
    pq.insert("Термінове питання", 50)
    pq.insert("Дуже важлива справа", 100) 
    pq.insert("Нова задача", 70)
    pq.insert("Нові значення", 120) 
    

    print(f"Найвищий пріоритет (peek): {pq.peek()}")
    print(f"Видаляємо: {pq.pop()}")
    print(f"Наступний на черзі: {pq.pop()}")