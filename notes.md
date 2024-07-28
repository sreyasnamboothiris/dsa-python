# Data Structures and Algorithms (DSA) Notes

## Introduction

### Data Strucures
- : Organizing the data in memory.

### Algorithms
- : A set of instructions to solve a problem.

## Characters of alogorithms
- **Input**
- **Output**
- **Unambiguity**
- **Finiteness**
- **Effectiveness**
- **Language independend**

### Complexity analyasis
- **Time Complexity** : How much time does it take to execute an algorithm.
- **Space Complexity** : How much space does it take to execute an algorithm.


### Time Complexity

Time complexity is a computational complexity that describes the amount of time it takes to run an algorithm as a function of the size of the input. It gives an estimate of the running time of an algorithm based on the number of basic operations executed.

**Steps to Determine Time Complexity:**
1. **Identify Basic Operations**: Find the basic operations in the algorithm (e.g., comparisons, assignments).
2. **Count the Operations**: Count how many times the basic operations are executed with respect to the input size `n`.
3. **Determine the Growth Rate**: Identify the dominant term as `n` grows large, which defines the time complexity in Big-O notation.

**Example: Linear Search**
```python
def linear_search(arr, target):
    for i in range(len(arr)):   # This loop runs n times, where n is len(arr)
        if arr[i] == target:    # Constant time operation
            return i
    return -1
```
- **O(1)**: Constant time
- **O(log n)**: Logarithmic time
- **O(n)**: Linear time
- **O(n log n)**: Linearithmic time
- **O(n^2)**: Quadratic time
- **O(2^n)**: Exponential time
- **O(n!)**: Factorial time

### Space Complexity of Data Types
- **Integer**: 4 bytes
- **Float**: 4 bytes
- **Double**: 8 bytes
- **Character**: 1 byte
- **Boolean**: 1 byte
- **String**: n bytes (where n is the length of the string)
- **Array**: n * size of element (where n is the number of elements in the array)
- **Linked List**: n * size of node (where n is the number of nodes in the linked list)
- **Tree**: n * size of node (where n is the number of nodes in the tree)
- **Graph**: n * size of node + m * size of edge (where n is the number of nodes and m is the number of edges)

### Complexity analysis - doing
- **Big O Notation**: It is used to describe the worst-case scenario of an algorithm's**
- **Big Omega Notation**: It is used to describe the best-case scenario of an algorithm's**
- **Big Theta Notation**: It is used to describe the average-case scenario of an algorithm's**

## Visualization of Complexities
+-----+    +---------+    +-----+    +-----------+    +--------+    +--------+    +-------+
| O(1)| -> | O(log n)| -> | O(n) | -> | O(n log n)| -> | O(n^2) | -> | O(2^n) | -> | O(n!) |
+-----+    +---------+    +-----+    +-----------+    +--------+    +--------+    +-------+

## basic example of showcase time and space complexity
# Finding the Maximum Element in an Array

## Algorithm
```python
def find_max(arr):
    max_element = arr[0] # O(1) space
    for element in arr: # O(n) iterations
        if element > max_element: # O(1) comparison
            max_element = element # O(1) assignment
    return max_element
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

# Data Structures

## 1. Array
An array is a linear data structure that stores a collection of elements of the same data type.

### Operations on Array:
- **Traversal:** Iterating through the elements of an array.
- **Insertion:** Adding an element to the array at a specific index.
- **Deletion:** Removing an element from the array at a specific index.
- **Searching:** Finding an element in the array by its value or index.

### Types of Arrays:
- **One-dimensional array:** A simple array with a single dimension.
- **Multidimensional array:** An array with multiple dimensions, such as a matrix.

### Applications of Array:
- Storing data in a sequential manner.
- Implementing queues, stacks, and other data structures.
- Representing matrices and tables.

## 2. String
A string is a sequence of characters, typically used to represent text. It allows for the manipulation and processing of textual data in computer programs.

### Operations on String:
- **Concatenation:** Joining two strings together.
- **Comparison:** Comparing two strings lexicographically.
- **Substring extraction:** Extracting a substring from a string.
- **Search:** Searching for a substring within a string.
- **Modification:** Changing or replacing characters within a string.

### Applications of String:
- Text processing.
- Pattern matching.
- Data validation.
- Database management.

## 3. Linked List
A linked list is a linear data structure that stores data in nodes, which are connected by pointers. Unlike arrays, linked lists are not stored in contiguous memory locations.

### Characteristics of Linked List:
- **Dynamic:** Linked lists can be easily resized by adding or removing nodes.
- **Non-contiguous:** Nodes are stored in random memory locations and connected by pointers.
- **Sequential access:** Nodes can only be accessed sequentially, starting from the head of the list.

### Operations on Linked List:
- **Creation:** Creating a new linked list or adding a new node to an existing list.
- **Traversal:** Iterating through the list and accessing each node.
- **Insertion:** Adding a new node at a specific position in the list.
- **Deletion:** Removing a node from the list.
- **Search:** Finding a node with a specific value in the list.

### Related Files
- [SingleLinkedList Operations](https://github.com/seyass/dsa-python/blob/main/operations/singlelinkedlist.py)

### Related Files
- [SingleLinkedList problems](https://github.com/seyass/dsa-python/blob/main/problems/)

### Types of Linked List:
- **Singly Linked List:** Each node points to the next node in the list.
- **Doubly Linked List:** Each node points to both the next and previous nodes in the list.
- **Circular Linked List:** The last node points back to the first node, forming a circular loop.

### Applications of Linked List:
- Implementing queues and stacks.
- Representing graphs and trees.
- Maintaining ordered data.
- Memory management.

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


 



 