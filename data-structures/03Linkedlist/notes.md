# Linked List
A linked list is a linear data structure that stores data in nodes, which are connected by pointers. Unlike arrays, linked lists are not stored in contiguous memory locations.

## Characteristics of Linked List:
- **Dynamic:** Linked lists can be easily resized by adding or removing nodes.
- **Non-contiguous:** Nodes are stored in random memory locations and connected by pointers.
- **Sequential access:** Nodes can only be accessed sequentially, starting from the head of the list.

## Operations on Linked List:
- **Creation:** Creating a new linked list or adding a new node to an existing list.
- **Traversal:** Iterating through the list and accessing each node.
- **Insertion:** Adding a new node at a specific position in the list.
- **Deletion:** Removing a node from the list.
- **Search:** Finding a node with a specific value in the list.


## Types of Linked List:
- **Singly Linked List:** Each node points to the next node in the list.
- **Doubly Linked List:** Each node points to both the next and previous nodes in the list.
- **Circular Linked List:** The last node points back to the first node, forming a circular loop.

## Applications of Linked List:
- Implementing queues and stacks.
- Representing graphs and trees.
- Maintaining ordered data.
- Memory management.

## Time Complexity:
- **Access:** O(n)
- **Search:** O(n)
- **Insertion (at head):** O(1)
- **Insertion (at tail):** O(1) (with a tail pointer), O(n) (without a tail pointer)
- **Insertion (at middle):** O(n)
- **Deletion (at head):** O(1)
- **Deletion (at tail):** O(n)
- **Deletion (at middle):** O(n)

## Space Complexity:
- **Space Complexity:** O(n) (for storing n elements)
- **Auxiliary Space:** O(1) (additional space used for pointers)

## Difference Between Array and Linked List

### Array:
- **Data Structure:** Contiguous.
- **Memory Allocation:** Typically allocated to the whole array.
- **Insertion/Deletion:** Inefficient.
- **Access:** Random.

### Linked List:
- **Data Structure:** Non-contiguous.
- **Memory Allocation:** Typically allocated one by one to individual elements.
- **Insertion/Deletion:** Efficient.
- **Access:** Sequential.
