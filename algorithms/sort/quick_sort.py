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
