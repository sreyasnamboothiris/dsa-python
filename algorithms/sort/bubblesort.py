# Bubble sort

array = [4, 3, 5, 3, 4, 5, 7, 6, 1, 3, 2]


def bubble_sort(array, reverse=False):
    size = len(array)
    for i in range(size):
        for j in range(size - i - 1):
            if reverse:
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            else:
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    return array

print(bubble_sort(array))

def bubble_sort_sting(string, reverse=False):
    string = list(string)
    size = len(string)
    for i in range(size):
        for j in range(size - i - 1):
            if reverse:
                if string[j] < string[j + 1]:
                    string[j], string[j + 1] = string[j + 1], string[j]
            else:
                if string[j] > string[j + 1]:
                    string[j], string[j + 1] = string[j + 1], string[j]
    new_string = ''
    for i in string:
        new_string += i
    return new_string

print(bubble_sort_sting('seras'))

class Node:

    def __init__(self, data):
        self.data = data
        self.ne

class LinkedList:

    def __int__(self):
        self.head = None
        self.tail = None

    def add_int_node(self, value):
        if type(value) != int:
            print('enter integer value')
            return
        node = Node(value)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def display(self):
        current_node = self.head
        if current_node is None:
            print('there is no value')
            return
        while current_node:
            print(current_node.data)
            current_node = current_node.next





