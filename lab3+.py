import os

class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def build_from_inverted_file(file_path: str):
        if not os.path.exists(file_path):
            print(f"Файл '{file_path}' не знайдено!")
            return None

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip().split() for line in f.readlines() if line.strip()][::-1]

        if not lines: return None

        root = BinaryTree(int(lines[0][0]))
        queue = [root]
        current_line_idx = 1

        while queue and current_line_idx < len(lines):
            level_values = lines[current_line_idx]
            next_queue = []
            val_idx = 0
            for node in queue:
                if val_idx < len(level_values):
                    val = level_values[val_idx]
                    if val.upper() != 'N':
                        node.left = BinaryTree(int(val))
                        next_queue.append(node.left)
                    val_idx += 1
                if val_idx < len(level_values):
                    val = level_values[val_idx]
                    if val.upper() != 'N':
                        node.right = BinaryTree(int(val))
                        next_queue.append(node.right)
                    val_idx += 1
            queue = next_queue
            current_line_idx += 1
        return root

    def display_pretty(self):
        """Метод для симетричного виведення дерева з гілками"""
        levels = []
        queue = [self]
        while any(queue):
            levels.append(queue)
            next_queue = []
            for node in queue:
                if node:
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                else:
                    next_queue.append(None)
                    next_queue.append(None)
            queue = next_queue
        
        levels = [l for l in levels if any(n is not None for n in l)]
        depth = len(levels)

        for i, level_nodes in enumerate(levels):
            step = 2 ** (depth - i - 1)
            
           
            line = ""
            for node in level_nodes:
                val = str(node.value) if node else " "
                line += val.center(step * 2)
            print(line)
            
           
            if i < depth - 1:
                branches = ""
                for node in level_nodes:
                    if node:
                        l = "/" if node.left else " "
                        r = "\\" if node.right else " "
                        branches += l.rjust(step) + r.ljust(step)
                    else:
                        branches += " " * (step * 2)
                print(branches)

if __name__ == "__main__":
    root = BinaryTree.build_from_inverted_file('tree.txt')
    if root:
        print("=== Дерево, збудоване з файлу ===")
        root.display_pretty()