
class BinaryTree: 
    def __init__(self, value: int): 
        self.value = value 
        self.left = None 
        self.right = None

def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
   
    if tree is None:
        return None
    
    
    tree.left, tree.right = tree.right, tree.left
    
  
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
    
    return tree



def print_tree(node, level=0, prefix="Root: "):
    """Допоміжна функція для візуалізації дерева в консолі"""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")



root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

print("Дерево ДО інверсії:")
print_tree(root)


invert_binary_tree(root)

print("\nДерево ПІСЛЯ інверсії:")
print_tree(root) 