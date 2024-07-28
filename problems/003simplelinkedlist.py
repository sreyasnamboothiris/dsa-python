# Problem 3: Find middle element of the linked list




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

def middle_element(linkedlist):
    current_node = linkedlist.head
    middle_node = linkedlist.head
    while current_node and current_node.next:
        current_node = current_node.next.next
        middle_node = middle_node.next
    return middle_node.data

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    data = middle_element(ll)
    print(f"The middle element is: {data}")
