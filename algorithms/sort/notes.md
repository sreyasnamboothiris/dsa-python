
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

## Insertion Sort

**Insertion Sort** is a simple comparison-based sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

**Steps of Insertion Sort:**

1. Start with the second element. Compare it with the first element and swap if necessary.
2. Move to the next element and compare it with the elements before it.
3. Insert the element into its correct position.
4. Repeat until the array is sorted.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)
```
**Time Complexity:**

- Best: O(n) (when the array is already sorted)
- Average: O(n²)
- Worst: O(n²)

**Space Complexity:**

- O(1) (in-place sorting)

## Quick Sort

**Quick Sort** is an efficient comparison-based sorting algorithm. It uses divide-and-conquer to gain the same advantages as merge sort, while not using additional storage.

**Steps of Quick Sort:**
1. Pick an element as a pivot.
2. Partition the array into two sub-arrays according to the pivot.
3. Recursively apply quicksort to the sub-arrays.

**Python Implementation:**
```python
array = [9, 33, 21, 47, 5, 9, 13, 99, 76]


def quick_sort(array):
    start = 0
    end = len(array) - 1
    sort(array, start, end)
    return array


def sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]

        if array[left] <= array[pivot]:
            left += 1

        if array[right] >= array[pivot]:
            right -= 1

    array[right], array[pivot] = array[pivot], array[right]
    sort(array, start, right - 1)
    sort(array, right + 1, end)


quick_sort(array)
print(array)

```
**Time Complexity:**
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n²) (when the pivot is the smallest or largest element)

**Space Complexity:**
- O(log n) (due to recursion stack)
- O(1) (in-place sorting)


## Merge Sort

**Merge Sort** is an efficient, stable, comparison-based sorting algorithm. Most implementations produce a stable sort, meaning that the implementation preserves the input order of equal elements in the sorted output.

**Steps of Merge Sort:**
1. Divide the unsorted list into `n` sublists, each containing one element.
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.

**Python Implementation:**

```python
array = [8, 5, 9, 1, 6]


def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    lef_array = merge_sort(array[:mid])
    rit_array = merge_sort(array[mid:])

    return merge(lef_array,rit_array)


def merge(left,right):

    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array = sorted_array + left[i:] + right[j:]
    return sorted_array

print(merge_sort(array))
```

**Time Complexity:**
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)

**Space Complexity:**
- O(n) (due to auxiliary space used for merging)
