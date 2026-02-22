# Red-Black Tree Implementation

This repository contains a Python implementation of a Red-Black Tree.

Currently implemented:
- Binary Search Tree (BST) insert
- Search operation
- Inorder traversal
- Basic test suite

Red-Black balancing is not yet implemented.

---

# 🌳 What Is a Binary Search Tree (BST)?

A Binary Search Tree is a binary tree where:

- Every node has at most two children.
- For any node:
  - All values in the left subtree are **less than** the node's key.
  - All values in the right subtree are **greater than or equal to** the node's key.

Example:

        10
       /  \
      5    20
     / \
    2   7

Why this matters:
- Search runs in O(h)
- Insert runs in O(h)
- If balanced, h ≈ log(n)

If not balanced, worst case becomes O(n).

---

# 🔍 Search Operation

Search works by repeatedly comparing the target key:

- If key < current node → go left
- If key > current node → go right
- If equal → found

Because of BST ordering, we eliminate half the tree at each step (if balanced).

Time Complexity:
- Average: O(log n)
- Worst case (skewed tree): O(n)

---

# 🔁 Inorder Traversal

Inorder traversal visits nodes in this order:

    Left → Node → Right

For a BST, this produces a **sorted list** of values.

Example:

Insert: [10, 20, 5, 15, 2, 7]

Inorder traversal output:

2, 5, 7, 10, 15, 20

Why this is powerful:
- It proves the BST property is correctly maintained.

---

# 🎨 What Is a Red-Black Tree?

A Red-Black Tree is a self-balancing BST with extra color rules.

Each node is either:
- Red
- Black

Red-Black Tree Properties:

1. Every node is either red or black.
2. The root is always black.
3. No two red nodes can be adjacent.
4. Every path from root to leaf has the same number of black nodes.
5. All leaves (NIL nodes) are black.

These rules guarantee:

Height ≤ 2 * log(n)

Which ensures:

- Search = O(log n)
- Insert = O(log n)
- Delete = O(log n)

Even in worst case.

---

# 🧪 Testing

Tests validate:

- Insert maintains BST ordering
- Inorder traversal produces sorted output
- Search finds existing values
- Search returns None for missing values
- Empty tree behavior
- Duplicate insertion behavior

To run tests:

    cd src
    python test_rb_tree.py

If successful, you will see:

✓ Insert + inorder test passed  
✓ Search test passed  
✓ Empty tree test passed  
✓ Duplicate insert test passed  

If something fails, an AssertionError will be raised.

---

# 📈 Time Complexity Summary

BST (unbalanced):
- Search: O(h)
- Insert: O(h)
- Worst case: O(n)

Red-Black Tree:
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

Because height is always logarithmic.

---

# 🚀 Next Steps

- Implement left rotation
- Implement right rotation
- Implement red-black insert fix-up
- Implement delete
- Add proper unit tests (pytest)
- Add performance benchmarking
- Add visualization

---

# 👩‍💻 Author

Anusha Maheshwari