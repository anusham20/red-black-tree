from rb_tree import RedBlackTree

def run_tests():
    tree = RedBlackTree()

    values = [10, 20, 5, 15, 2, 7]
    for v in values:
        tree.insert(v)

    print("Inorder traversal (should be sorted):")
    tree.inorder(tree.root)

    # Test search
    print("\nSearch Tests:")
    result = tree.search(15)
    if result:
        print("Found 15")
    else:
        print("15 not found")

    result = tree.search(100)
    if result:
        print("Found 100")
    else:
        print("100 not found")


if __name__ == "__main__":
    run_tests()