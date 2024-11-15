j = [3, 4, 6, 7, 8, 9, 87, 89, 90, 91]


def binary_search(array, number):
    start = 0
    end = len(array) - 1
    mid = len(array) // 2

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == number:
            return number
        elif array[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return False


print(binary_search(j, 87))
