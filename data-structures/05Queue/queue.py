# Queue using linked list

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

    def enqueue(self, data):
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
        val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return val

    def peek(self):
        return self.front.data


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.display()
queue.dequeue()
queue.display()


# Queue using Stack(array)

class QueueUsingStack:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, data):
        self.stack_1.append(data)

    def peek(self):

        if self.stack_2:
            return self.stack_2[-1]

        return self.stack_1[0]

    def pop(self):

        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()


qu = QueueUsingStack()

qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
print(qu.peek())
j = qu.pop()
print(j)
print(qu.peek())
print("#############################")
qu.enqueue(5)
print(qu.peek())
print(qu.pop())
qu.enqueue(6)
print(qu.pop())
qu.enqueue(7)
print(qu.pop())
print(qu.pop())


