class Node:
    def __init__(self, key, color="red"):
        self.key = key
        self.color = color  # "red" or "black"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    # Basic BST Insert
    def insert(self, key):
        new_node = Node(key)

        # Case 1: Tree is empty
        if self.root is None:
            self.root = new_node
            self.root.color = "black"  # root must be black in RB tree
            return

        # Otherwise find correct position
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    # Search
    def search(self, key):
        current = self.root
        while current is not None and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    # Inorder Traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f"{node.key} ({node.color})")
            self.inorder(node.right)