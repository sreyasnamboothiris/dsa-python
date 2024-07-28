
# stack in linkedlist

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None


    def display(self):
        current_node = self.top
        if current_node is None:
            print('there is no data')
            return
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

    def pop(self):

        if self.top:
            self.top = self.top.next
        else:
            print('there is no data')
            return

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "There is no data"




stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
stack.pop()
stack.display()
k = stack.peek()
print(k)







