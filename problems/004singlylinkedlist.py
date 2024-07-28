# Problem 4: Selection Sort for a Singly Linked List
# Question: How can we sort a singly linked list using the selection sort algorithm?

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A LinkedList class for creating and managing a singly linked list.

    Attributes:
    head (Node): The head node of the list.
    tail (Node): The tail node of the list.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_int_node(self, data):
        """
        Adds a new node with integer data to the end of the list.

        Parameters:
        data (int): The data to be added to the list.
        """
        if type(data) != int:
            print('Please enter an integer value')
            return
        node = Node(data)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def display(self):
        """
        Displays the data in the linked list.
        """
        current_node = self.head
        if current_node is None:
            print('There are no values')
            return
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def selection_sort(self):
        """
        Sorts the linked list using the selection sort algorithm.
        """
        start = self.head
        if self.head is None:
            print('There is no data')
            return
        while start:
            current_node = start.next
            min_node = start
            while current_node:
                if current_node.data < min_node.data:
                    min_node = current_node
                current_node = current_node.next

            if min_node != start:
                start.data, min_node.data = min_node.data, start.data
            start = start.next


# Example usage of LinkedList with selection sort
link = LinkedList()
link.add_int_node(3)
link.add_int_node(2)
link.add_int_node(8)
link.add_int_node(1)
link.add_int_node(4)
print("Original Linked List:")
link.display()
link.selection_sort()
print("Sorted Linked List:")
link.display()