arr = ["apple", "orange", "banana", "grape", "cherry"]


def insertion_sort(array):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array




print(insertion_sort([3,2,1,5,6,4,3,2]))



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

k = [(',',{ 56 }),({76},)]
print(k)