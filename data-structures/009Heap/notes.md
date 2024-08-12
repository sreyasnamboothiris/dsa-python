# Heap

A heap is a specialized tree-based data structure that satisfies the heap property. It is commonly used to implement priority queues.

## Characteristics of Heap:
- **Binary Heap:** A complete binary tree where each node is greater than or equal to (max-heap) or less than or equal to (min-heap) its children.
- **Heap Property:** 
  - **Max-Heap:** The value of each node is greater than or equal to the values of its children.
  - **Min-Heap:** The value of each node is less than or equal to the values of its children.
- **Complete Binary Tree:** All levels are completely filled except possibly for the last level, which is filled from left to right.

## Types of Heaps:
- **Max-Heap:** The root node is the maximum element in the heap.
- **Min-Heap:** The root node is the minimum element in the heap.

## Operations on Heaps:
- **Insertion:** Adding a node to the heap.
  - **Time Complexity:** O(log n)
  - **Space Complexity:** O(1)
- **Deletion:** Removing the root node from the heap.
  - **Time Complexity:** O(log n)
  - **Space Complexity:** O(1)
- **Peek:** Getting the value of the root node without removing it.
  - **Time Complexity:** O(1)
  - **Space Complexity:** O(1)
- **Heapify:** Arranging an array of elements into a heap.
  - **Time Complexity:** O(n)
  - **Space Complexity:** O(1)

## Traversal of Heaps:
- **Level-order Traversal:** Visiting nodes level by level from top to bottom.

## Applications of Heaps:
- **Priority Queues:** Implementing queues where each element has a priority.
- **Heap Sort:** An efficient sorting algorithm.
- **Graph Algorithms:** Finding the shortest path (Dijkstra’s algorithm) and minimum spanning tree (Prim’s algorithm).
- **Order Statistics:** Finding the k-th smallest (or largest) element in an array.

## Properties of Heaps:
- **Height of Heap:** The height of a heap with n nodes is ⌊log₂n⌋.
- **Maximum Number of Nodes:** A heap of height h has at most 2^(h+1) - 1 nodes.
- **Minimum Number of Nodes:** A heap of height h has at least 2^h nodes.

## Summary:
Heaps are versatile data structures used in various applications, especially those requiring dynamic ordering or priority. Their properties and efficient operations make them suitable for implementing priority queues, sorting algorithms, and several graph algorithms.

## Examples of Heap Operations:

### Insertion in a Max-Heap:
1. Insert the new element at the end of the heap.
2. Compare the inserted element with its parent; if the inserted element is greater, swap them.
3. Repeat step 2 until the heap property is restored.

### Deletion in a Max-Heap:
1. Replace the root element with the last element in the heap.
2. Remove the last element.
3. Compare the new root with its children; if the new root is smaller, swap it with the larger child.
4. Repeat step 3 until the heap property is restored.

## Heap Sort Algorithm:
1. Build a max-heap from the input data.
2. Swap the root (maximum value) of the heap with the last element.
3. Reduce the heap size by one and heapify the root element to restore the heap property.
4. Repeat steps 2-3 until the heap size is greater than one.
  - **Time Complexity:** O(n log n)
  - **Space Complexity:** O(1)
