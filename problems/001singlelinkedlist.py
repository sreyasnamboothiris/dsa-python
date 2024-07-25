"""Write a function to get Nth node in a Linked List"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

def n_th_node(linkedlist, n):
    current_node = linkedlist.head
    number = 1
    if n == 1:
        return current_node
    while current_node and n != number:
        number += 1
        current_node = current_node.next
    if current_node:
        return current_node
    print('Invalid position')
    return

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    node = n_th_node(ll, 3)
    if node:
        print(f"The {3}rd node is: {node.data}")


