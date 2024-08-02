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