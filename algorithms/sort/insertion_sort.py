arr = ["apple", "orange", "banana", "grape", "cherry"]

i = 1


def insertion_sort(array):
    for i in range(len(array)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return array


print(insertion_sort(arr))


def insertion_sort_strings(array):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j <= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        return

    def display(self):
        if self.head is None:
            print('there is no data')
            return
        current_node = None
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        return

    def insertion_sort(self):
        current_node = self.head
        if current_node is None:
            print('there is no data')
            return


