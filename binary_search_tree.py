"""A binary search tree (BST) is a type of binary tree where each node has at most two children, an left child and a right child. Each node in the tree represents a value and all values to the left of it are less than the value itself."""
import sys

def Node(value):
    """A simple binary search tree node."""
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
    """A simple binary search tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Recursive insertion of a value into the BST."""
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = Node(value)
    
    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Recursive search for a value in the BST."""
        if not node:
            return None
        elif value == node.value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """Return the nodes in the BST in order."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Recursive inorder traversal of the BST."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in range(10):
        bst.insert(i)
    print(bst.inorder())
