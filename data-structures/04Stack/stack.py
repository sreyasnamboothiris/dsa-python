#
# # stack in linkedlist
#
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Stack:
#
#     def __init__(self):
#         self.top = None
#
#
#     def display(self):
#         current_node = self.top
#         if current_node is None:
#             print('there is no data')
#             return
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next
#
#     def push(self,data):
#         node = Node(data)
#         if self.top:
#             node.next = self.top
#             self.top = node
#         else:
#             self.top = node
#
#     def pop(self):
#
#         if self.top:
#             self.top = self.top.next
#         else:
#             print('there is no data')
#             return
#
#     def peek(self):
#         if self.top:
#             return self.top.data
#         else:
#             return "There is no data"
#
#     def is_empty(self):
#         if self.top is None:
#             return True
#         else:
#             return False
#
# class StackArray:
#
#     def __init__(self):
#         self.items = []
#
#     def push(self,item):
#         self.items.append(item)
#
#     def pop(self):
#         self.items.pop()
#
#     def peek(self):
#         if self.items:
#             return self.items[-1]
#         return None
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.display()
# stack.pop()
# stack.display()
# k = stack.peek()
# print(k)
# print(stack.is_empty())
#
#
from queue import Queue


class StackUsingQueue:

    def __init__(self):
        self.que1 = Queue()
        self.que2 = Queue()

    def push(self, data):
        self.que2.enqueue(data)

        while self.que1.front:
            self.que2.enqueue(self.que1.dequeue())
        self.que2, self.que1 = self.que1, self.que2

    def display(self):
        self.que1.display()
        return

    def peek(self):
        return self.que1.peek()


s = StackUsingQueue()
s.push('sreyas')
s.push('sreejesh')
s.push('sreedevi')
print(s.peek())
s.display()

