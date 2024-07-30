
array = [1,4,3,2,39,5,6,90,3,32,12]

def insertion_sort(array,reverse = False):

    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        if reverse:
            while j >= 0 and array[j] < key:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
        else:
            while j >= 0 and array[j] > key:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
    return array

print(insertion_sort(array,reverse=True))


