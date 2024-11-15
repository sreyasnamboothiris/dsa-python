
class Node:

    def __init__(self,data):
        self.data = data
        self.next = self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert(self,data):

        if self.head is None:
            self.head = Node(data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        new_node = Node(data)
        new_node.prev = current_node
        current_node.next = new_node


