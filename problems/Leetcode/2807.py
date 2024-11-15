#
# 2807. Insert Greatest Common Divisors in Linked List
# Medium

# Given the head of a linked list head, in which each node contains an integer value.
# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
# Return the linked list after insertion.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

class Node:

    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add_element(self,data):
        current_node = self.head
        if current_node is None:
            self.head = Node(data)
            return
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)
        return

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end=' -> ' if current_node.next else '')
            current_node = current_node.next
        print()

    def find_gcd(self,a,b):
        while b:
            a, b = b, a%b
        return a

    def insert_gcd(self):
        current_node = self.head
        if current_node is None:
            return
        while current_node.next:
            gcd_val = self.find_gcd(current_node.val,current_node.next.val)
            gcd_node = Node(gcd_val)
            gcd_node.next = current_node.next
            current_node.next = gcd_node
            current_node = gcd_node.next



link = LinkedList()
link.add_element(18)
link.add_element(6)
link.add_element(10)
link.add_element(3)
link.display()
link.insert_gcd()
link.display()

