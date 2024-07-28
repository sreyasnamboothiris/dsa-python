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
# Sorting Algorithms

## Selection Sort

**Selection Sort** is a simple comparison-based sorting algorithm. It has an average and worst-case time complexity of O(n²), making it inefficient on large lists. However, it performs well on small lists and has the advantage of being easy to implement.

**Steps of Selection Sort:**
1. Find the minimum element in the unsorted part of the array.
2. Swap it with the first element of the unsorted part.
3. Move the boundary of the sorted part one element to the right.
4. Repeat until the array is sorted.

**Python Implementation:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
```

**Time Complexity:**
- Best: O(n²)
- Average: O(n²)
- Worst: O(n²)

**Space Complexity:**
- O(1) (in-place sorting)

## Bubble Sort

**Bubble Sort** is another simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

**Steps of Bubble Sort:**
1. Compare the first two elements. If the first is greater than the second, swap them.
2. Move to the next pair of elements, and repeat step 1.
3. Continue until the end of the list is reached.
4. Repeat the process for the entire list until no swaps are needed.

**Python Implementation:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
```

**Time Complexity:**
- Best: O(n) (when the array is already sorted)
- Average: O(n²)
- Worst: O(n²)

**Space Complexity:**
- O(1) (in-place sorting)



