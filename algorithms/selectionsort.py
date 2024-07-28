# selection sort,


array = [3,5,6,2,3,6]

def selection_sort(array, reverse=False):

    size = len(array)
    if reverse:
        for i in range(size-1):
            for j in range(i+1,size):
                if array[j] > array[i]:
                    array[j],array[i] = array[i],array[j]
        return array
    for i in range(size-1):
        for j in range(i+1,size):
            if array[i] > array[j]:
                array[i],array[j] = array[j],array[i]
    return array

print(selection_sort(array,reverse=True))

####################################
# selection sort for singlylinkedlist
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_int_node(self,data):
        if type(data) != int:
            print('please enter a integer value')
            return
        node = Node(data)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def display(self):
        current_node = self.head
        if current_node is None:
            print('there is no values')
            return
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def selection_sort(self):
        start = self.head
        if self.head is None:
            print('there is no data')
            return
        while start:
            current_node = start.next
            min = start
            while current_node:
                if current_node.data < min.data:
                    min = current_node
                current_node = current_node.next

            if min != start:
                start.data, min.data = min.data, start.data
            start = start.next


link = LinkedList()
link.add_int_node(3)
link.add_int_node(2)
link.add_int_node(8)
link.add_int_node(1)
link.add_int_node(4)
#link.display()
link.selection_sort()
#link.display()

########################################################

# string sort

def selection_sort_string(key):

    if type(key) != str:
        print('please enter a string')
        return
    new_key = ''
    key = list(key)
    size = len(key)
    for i in range(size):
        for j in range(i+1,size):
            if key[i] > key[j]:
                key[i],key[j] = key[j],key[i]
    for i in key:
        new_key += i

    return new_key


print(selection_sort_string('sreyas'))







