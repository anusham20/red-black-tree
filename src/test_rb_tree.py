from rb_tree import RedBlackTree


def test_insert_and_inorder():
    tree = RedBlackTree()
    values = [10, 20, 5, 15, 2, 7]
    for v in values:
        tree.insert(v)

    result = []
    collect_inorder(tree.root, result)

    assert result == sorted(values), "Inorder traversal failed"
    print("✓ Insert + inorder test passed")


def test_search():
    tree = RedBlackTree()
    values = [10, 20, 5]
    for v in values:
        tree.insert(v)

    assert tree.search(20) is not None, "Search failed for existing value"
    assert tree.search(100) is None, "Search failed for missing value"
    print("✓ Search test passed")


def collect_inorder(node, result):
    if node is not None:
        collect_inorder(node.left, result)
        result.append(node.key)
        collect_inorder(node.right, result)


if __name__ == "__main__":
    test_insert_and_inorder()
    test_search()