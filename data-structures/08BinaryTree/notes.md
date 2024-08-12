# Binary Tree

A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child.

## Characteristics of Binary Tree:
- **Root:** The topmost node in a binary tree.
- **Node:** Each element in the binary tree.
- **Edge:** A connection between two nodes.
- **Leaf:** A node with no children.
- **Subtree:** A tree formed by a node and its descendants.
- **Height:** The length of the longest path from the root to a leaf.
- **Depth:** The length of the path from the root to a node.

## Types of Binary Trees:
- **Full Binary Tree:** Each node has either 0 or 2 children.
- **Complete Binary Tree:** All levels are completely filled except possibly for the last level, which is filled from left to right.
- **Perfect Binary Tree:** All internal nodes have two children, and all leaves are at the same level.
- **Balanced Binary Tree:** The height of the two subtrees of any node differ by at most one.
- **Degenerate (or Pathological) Tree:** Each parent node has only one child.

## Operations on Binary Trees:
- **Insertion:** Adding a node to the binary tree.
  - **Time Complexity:** O(n)
  - **Space Complexity:** O(1) (iterative), O(h) (recursive, where h is the height of the tree)
- **Deletion:** Removing a node from the binary tree.
  - **Time Complexity:** O(n)
  - **Space Complexity:** O(1) (iterative), O(h) (recursive, where h is the height of the tree)
- **Traversal:** Visiting all the nodes in a specific order.
  - **In-order Traversal:** Left, Root, Right
    - **Time Complexity:** O(n)
    - **Space Complexity:** O(h) (where h is the height of the tree)
  - **Pre-order Traversal:** Root, Left, Right
    - **Time Complexity:** O(n)
    - **Space Complexity:** O(h) (where h is the height of the tree)
  - **Post-order Traversal:** Left, Right, Root
    - **Time Complexity:** O(n)
    - **Space Complexity:** O(h) (where h is the height of the tree)
  - **Level-order Traversal:** Level by level from top to bottom
    - **Time Complexity:** O(n)
    - **Space Complexity:** O(n)

## Applications of Binary Trees:
- **Expression Trees:** Representing arithmetic expressions.
- **Hierarchical Data Representation:** Organization charts, file systems.
- **Binary Search Trees:** Efficient searching, insertion, and deletion.
- **Heaps:** Implementing priority queues.
- **Huffman Coding Tree:** Data compression algorithms.

## Properties of Binary Trees:
- **Maximum Number of Nodes:** A binary tree of height h has at most 2^(h+1) - 1 nodes.
- **Minimum Height:** The minimum height of a binary tree with n nodes is ⌈log₂(n + 1)⌉ - 1.
- **Minimum Number of Nodes:** A binary tree of height h has at least h + 1 nodes.

## Summary:
Binary trees are fundamental data structures used in various applications, from representing hierarchical data to implementing efficient searching and sorting algorithms. Understanding their properties and operations is essential for optimizing performance in computer science and software engineering tasks.


# Binary Search Tree (BST)

A Binary Search Tree (BST) is a binary tree in which each node has a value such that:
- The value of the left child is less than the value of the parent node.
- The value of the right child is greater than the value of the parent node.
- This property holds true for all nodes in the tree.

## Characteristics of Binary Search Tree:
- **Root:** The topmost node in the BST.
- **Node:** Each element in the BST.
- **Edge:** A connection between two nodes.
- **Leaf:** A node with no children.
- **Subtree:** A tree formed by a node and its descendants.
- **Height:** The length of the longest path from the root to a leaf.
- **Depth:** The length of the path from the root to a node.
- **BST Property:** For any node with value `x`, all values in the left subtree are less than `x` and all values in the right subtree are greater than `x`.

## Operations on Binary Search Trees:
- **Search:** Finding a node with a specific value in the BST.
  - **Time Complexity:** O(h) (where h is the height of the tree)
  - **Space Complexity:** O(1) (iterative), O(h) (recursive)
- **Insertion:** Adding a new node to the BST while maintaining its properties.
  - **Time Complexity:** O(h) (where h is the height of the tree)
  - **Space Complexity:** O(1) (iterative), O(h) (recursive)
- **Deletion:** Removing a node from the BST while maintaining its properties.
  - **Time Complexity:** O(h) (where h is the height of the tree)
  - **Space Complexity:** O(1) (iterative), O(h) (recursive)
  - **Cases in Deletion:**
    - **Node with no children:** Simply remove the node.
    - **Node with one child:** Remove the node and replace it with its child.
    - **Node with two children:** Replace the node with its in-order successor (smallest value in the right subtree) or in-order predecessor (largest value in the left subtree).

- **Traversal:** Visiting all the nodes in a specific order.
  - **In-order Traversal:** Left, Root, Right (yields nodes in non-decreasing order)
    - **Time Complexity:** O(n)
    - **Space Complexity:** O(h) (where h is the height of the tree)
  - **Pre-order Traversal:** Root, Left, Right
    - **Time Complexity:** O(n)
    - **Space Complexity:** O(h) (where h is the height of the tree)
  - **Post-order Traversal:** Left, Right, Root
    - **Time Complexity:** O(n)
    - **Space Complexity:** O(h) (where h is the height of the tree)
  - **Level-order Traversal:** Level by level from top to bottom
    - **Time Complexity:** O(n)
    - **Space Complexity:** O(n)

## Properties of Binary Search Trees:
- **In-order Traversal Property:** An in-order traversal of a BST yields the nodes in sorted (non-decreasing) order.
- **Height of BST:** The height of a BST with `n` nodes is `O(log n)` for a balanced tree and `O(n)` for a skewed tree.
- **Minimum Value Node:** The leftmost node in the BST (keep moving left until you find a node with no left child).
- **Maximum Value Node:** The rightmost node in the BST (keep moving right until you find a node with no right child).

## Applications of Binary Search Trees:
- **Searching:** Efficiently finding elements in sorted order.
- **Sorting:** In-order traversal of BST can be used to sort elements.
- **Dynamic Sets:** BSTs allow dynamic insertion and deletion while maintaining order.
- **Database Indexing:** BSTs are used to implement indexes for efficient data retrieval.

## Summary:
Binary Search Trees are a fundamental data structure used in various applications where efficient searching, insertion, and deletion are required. Understanding the properties and operations of BSTs is crucial for solving many computer science problems related to data organization and retrieval.

