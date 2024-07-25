
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# add a node at end
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def delete_node(self, data):
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            return
        prev = None
        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next
        if data == self.tail.data:
            self.tail = prev
            self.tail.next = None
            return
        if temp is None:
            return
        prev.next = temp.next

# insert a data after a key
    def insert_after(self, next_to, data):
        new_node = Node(data)
        temp = self.head
        prev = None
        while temp is not None and temp.data != next_to:
            temp = temp.next
        if temp is None:
            return
        if next_to == self.tail.data:
            self.tail.next = new_node
            self.tail = new_node
            return
        new_node.next = temp.next
        temp.next = new_node
        return

# insert a data before a key
    def insert_before(self, prev_to, data):
        temp = self.head
        new_node = Node(data)
        prev = None
        if prev_to == temp.data:
            new_node.next = self.head
            self.head = new_node
            return
        while temp is not None and prev_to != temp.data:
            prev = temp
            temp = temp.next
        if self.tail.data == prev_to:
            self.tail.next = new_node
            self.tail = new_node
            return
        if prev is None:
            return
        new_node.next = prev.next
        prev.next = new_node

# add data on the fist position(head)
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

# show case the data
    def display_data(self):
        if self.head is None:
            print('there is no data')
            return
        current_node = self.head
        while current_node is not None:
            print('data: ', current_node.data)
            current_node = current_node.next

linkedlist = SLinkedList()
linkedlist.add_node(1)
linkedlist.push(2)
linkedlist.display_data()