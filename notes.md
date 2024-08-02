# Data Structures and Algorithms (DSA) Notes

## Introduction

### Data Structures
- : Organizing the data in memory.

### Algorithms
- : A set of instructions to solve a problem.

## Characters of algorithms
- **Input**
- **Output**
- **Unambiguity**
- **Finiteness**
- **Effectiveness**
- **Language independent**

### Complexity analysis
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





 



 