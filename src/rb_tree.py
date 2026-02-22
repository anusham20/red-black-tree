class Node:
    def __init__(self, key, color="red"):
        self.key = key
        self.color = color  # "red" or "black"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color="black")
        self.root = self.NIL

    def insert(self, key):
        print(f"Inserting {key}")
        # we will implement this next

    def search(self, key):
        current = self.root
        while current != self.NIL and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current