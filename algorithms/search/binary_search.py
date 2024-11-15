

arr = [1, 2, 4, 6, 7, 8]

def binary_search(array,key):

    left = 0
    right = len(array)
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            return key
        elif array[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return 'no element found'

print(binary_search(arr,2))


