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
