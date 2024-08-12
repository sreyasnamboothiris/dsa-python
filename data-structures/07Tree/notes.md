# Tree Structure

A tree is a hierarchical data structure consisting of nodes, with a single node called the root and zero or more child nodes. Each node can have zero or more child nodes, forming a tree-like structure.

## Characteristics of Tree:
- **Root:** The topmost node in a tree.
- **Node:** Each element in the tree.
- **Edge:** A connection between two nodes.
- **Leaf:** A node with no children.
- **Subtree:** A tree formed by a node and its descendants.
- **Height:** The length of the longest path from the root to a leaf.
- **Depth:** The length of the path from the root to a node.

## Types of Trees:
- **Binary Tree:** Each node has at most two children.
- **Binary Search Tree (BST):** A binary tree where the left child is less than the parent node, and the right child is greater.
- **Balanced Tree:** A tree where the height of the two subtrees of any node differ by at most one.
- **AVL Tree:** A self-balancing binary search tree.
- **Red-Black Tree:** A self-balancing binary search tree with additional properties.
- **B-Tree:** A self-balancing search tree for databases and file systems.
- **Heap:** A complete binary tree where the parent node is either greater than (max-heap) or less than (min-heap) its children.

## Operations on Trees:
- **Insertion:** Adding a node to the tree.
- **Deletion:** Removing a node from the tree.
- **Traversal:** Visiting all the nodes in a specific order.
  - **In-order Traversal:** Left, Root, Right
  - **Pre-order Traversal:** Root, Left, Right
  - **Post-order Traversal:** Left, Right, Root
  - **Level-order Traversal:** Level by level from top to bottom

## Applications of Trees:
- **Hierarchical Data Representation:** Organization charts, file systems.
- **Binary Search Tree:** Efficient searching, insertion, and deletion.
- **Expression Trees:** Representing arithmetic expressions.
- **Huffman Coding Tree:** Data compression algorithms.
- **B-Trees and Variants:** Database indexing.
- **Heaps:** Priority queues.

## Operations on Trees:
- **Insertion:** Adding a node to the tree.
  - Time Complexity: O(log n) for balanced trees, O(n) for unbalanced trees.
- **Deletion:** Removing a node from the tree.
  - Time Complexity: O(log n) for balanced trees, O(n) for unbalanced trees.
- **Traversal:** Visiting all the nodes in a specific order.
  - Time Complexity: O(n)

