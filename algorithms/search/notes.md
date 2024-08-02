# Searching Algorithms

## Linear Search

### Description
Linear search is a simple search algorithm that checks each element in the list one by one until the target element is found or the list ends.

### Steps
1. Start from the first element in the list.
2. Compare each element with the target element.
3. If the target element is found, return its position.
4. If the target element is not found after checking all elements, return -1.

### Time Complexity
- **Best Case**: O(1) - The target element is at the beginning of the list.
- **Average Case**: O(n) - The target element is somewhere in the middle of the list.
- **Worst Case**: O(n) - The target element is at the end of the list or not present at all.

### Example Code (Python)
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [2, 4, 0, 1, 9]
target = 1
result = linear_search(arr, target)
print(f'Target found at index: {result}')  # Output: Target found at index: 3
```
## Binary Search

### Description
Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half and comparing the middle element with the target value.

### Steps
1. Start with the middle element of the sorted array.
2. If the middle element is equal to the target element, return its position.
3. If the target element is smaller than the middle element, narrow the search to the left half.
4. If the target element is larger than the middle element, narrow the search to the right half.
5. Repeat steps 1-4 until the target element is found or the search interval is empty.

### Time Complexity
- **Best Case**: O(1) - The target element is at the middle of the list.
- **Average Case**: O(log n) - The search interval is divided in half each time.
- **Worst Case**: O(log n) - The search interval is divided in half each time.

### Space Complexity
- **O(1)** - Binary search requires a constant amount of additional space.

### Example Code (Python)
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [0, 1, 2, 4, 9]
target = 4
result = binary_search(arr, target)
print(f'Target found at index: {result}')  # Output: Target found at index: 3
```