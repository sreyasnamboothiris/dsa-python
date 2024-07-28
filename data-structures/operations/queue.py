class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def display(self):
        current_node = self.front
        if self.front == None:
            print('there is no data')
            return
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def enqueue(self,data):
        node = Node(data)
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node
        return

    def dequeue(self):
        if self.front is None:
            print('there is no data')
            return
        self.front = self.front.next
        if self.front is None:
            self.rear = None


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.display()
queue.dequeue()
queue.display()

