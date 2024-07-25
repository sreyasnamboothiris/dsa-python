"""Nth node from the end of a Linked List"""

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

def n_th_node_end(linkedlist, n):
    current_node = linkedlist.head
    back_node = linkedlist.head
    count = 0
    while count != n and current_node:
        current_node = current_node.next
        count += 1
    if current_node is None and count < n:
        return "There is no data"
    while current_node:
        back_node = back_node.next
        current_node = current_node.next
    return back_node.data if back_node else "There is no data"

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    data = n_th_node_end(ll, 2)
    print(f"The 2nd node from the end is: {data}")
