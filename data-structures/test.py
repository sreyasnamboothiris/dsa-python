#
# # array = [1,4,2,3,46,4,31,1,3,467,4,3,24,2]
# #
# # def quick_sort(array):
# #     start = 0
# #     end = len(array) - 1
# #     partetion(array,start,end)
# #     return array
# #
# # def partetion(array,start,end):
# #
# #     if start > end:
# #         return
# #
# #     pivot = start
# #     left = start +1
# #     right = end
# #     while left <= right:
# #         if array[left] > array[pivot] > array[right]:
# #             array[left], array[right] = array[right], array[left]
# #             left += 1
# #             right -= 1
# #
# #         if array[left] <= array[pivot]:
# #             left += 1
# #         if array[right] >= array[pivot]:
# #             right -= 1
# #
# #     array[right], array[pivot] = array[pivot], array[right]
# #     partetion(array,start,right-1)
# #     partetion(array,right+1,end)
# #
# #
# # print('this is quick sort',quick_sort(array))
# #
# #
# # def merge_sort(array):
# #
# #     if len(array) <= 1:
# #         return array
# #
# #     mid = len(array)//2
# #     right = merge_sort(array[mid:])
# #     left = merge_sort(array[:mid])
# #     return merge(right,left)
# #
# # def merge(right,left):
# #
# #     sorted_array = []
# #     i = 0
# #     j = 0
# #     while i < len(right) and j < len(left):
# #
# #         if right[i] >= left[j]:
# #             sorted_array.append(left[j])
# #             j += 1
# #         else:
# #             sorted_array.append(right[i])
# #             i += 1
# #     sorted_array.extend(right[i:])
# #     sorted_array.extend(left[j:])
# #     return sorted_array
# #
# # print('this is merge sort',merge_sort(array))
# #
# #
# # def insertion_sort(array):
# #
# #     for i in range(1,len(array)):
# #         key = array[i]
# #         j = i - 1
# #         while key < array[j] and j >= 0:
# #             array[j] = array[j+1]
# #             j -= 1
# #         array[j+1] = key
# #     return array
# #
# # print('this is insertion sort',insertion_sort(array))
# #
# # def selection_sort(array):
# #
# #     for i in range(len(array)):
# #         for j in range(i+1,len(array)):
# #             if array[i] > array[j]:
# #                 array[i], array[j] = array[j], array[i]
# #     return array
# #
# # print('this is selection sort',selection_sort(array))
# #
# # def bubble_sort(arary):
# #
# #     for i in range(len(array) - 1):
# #         for j in range(len(array) - i - 1):
# #             if arary[j] > array[j+1]:
# #                 array[j],array[j+1] = array[j+1], array[j]
# #
# #     return array
# #
# # print('this is bubble sort',bubble_sort(array))
#
#
#
#
#
# class Stack:
#
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         if len(self.items) == 0:
#             return True
#         else:
#             return False
#
#     def push(self,value):
#
#         self.items.append(value)
#
#     def pop(self):
#         if self.is_empty():
#             print('there is no data')
#             return
#         return self.items.pop()
#
#     def peek(self):
#         if self.is_empty():
#             print('there is no data')
#             return
#         return self.items[-1]
#
#     def display(self):
#         if self.is_empty():
#             print('there is no data')
#             return
#         for i in range(len(self.items)-1,-1,-1):
#             print(self.items[i],end=' => ' if i > 0 else '')
#         print()
#         return
#
#
# # stack = Stack()
# # stack.display()
# # print(stack.pop())
# # print(stack.peek())
# # stack.push(1)
# # stack.push(2)
# # stack.push(3)
# # stack.display()
# # print('pop',stack.pop())
# # stack.display()
# # print(stack.peek())
#
# class Node:
#
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class LinkedListStack:
#
#     def __init__(self):
#         self.top = None
#
#     def is_empty(self):
#         if self.top is None:
#             return True
#         else:
#             return False
#
#     def push(self,data):
#         node = Node(data)
#         if self.top:
#             node.next = self.top
#         self.top = node
#
#     def pop(self):
#         if self.is_empty():
#             print('there is no data')
#             return
#         value = self.top.data
#         self.top = self.top.next
#         return value
#
#     def peek(self):
#         if self.is_empty():
#             print('there is no data')
#             return
#         return self.top.data
#
#     def display(self):
#         if self.is_empty():
#             print('there is no data')
#             return
#         current_node = self.top
#         while current_node:
#             print(current_node.data, end=' => ' if current_node.next else '')
#             current_node = current_node.next
#         print()
#
#
#
# # stack = LinkedListStack()
# #
# # stack.display()
# # stack.push(1)
# # stack.push(2)
# # stack.push(3)
# # stack.display()
# # print(stack.pop())
# # print(stack.peek())
# # stack.display()
#
# class Queue:
#
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         if len(self.items) == 0:
#             print('there is no data')
#             return True
#         else:
#             return False
#
#     def enqueue(self,data):
#
#         self.items.append(data)
#
#     def dequeue(self):
#         if self.is_empty():
#             return
#         return self.items.pop(0)
#
#     def peek(self):
#         if self.is_empty():
#             return
#         return self.items[0]
#
#     def display(self):
#         if self.is_empty():
#             return
#
#         for i in range(len(self.items)):
#             print(self.items[i],end=' -> ' if i < len(self.items)-1 else '')
#
#         print()
#
#
# # queue = Queue()
# # queue.display()
# # queue.enqueue(1)
# # queue.enqueue(2)
# # queue.enqueue(3)
# # queue.display()
# # print(queue.peek())
# # print(queue.dequeue())
# # queue.display()
#
# class LinkedListQueue:
#
#     def __init__(self):
#         self.front = None
#         self.rear = None
#
#     def is_empty(self):
#         if self.front is None:
#             print('there is nodata')
#             return True
#         else:
#             return False
#
#     def enqueue(self,data):
#         node = Node(data)
#         if self.front:
#             self.rear.next = node
#         else:
#             self.front = node
#         self.rear = node
#
#     def dequeue(self):
#
#         if self.is_empty():
#             return
#         val = None
#         if self.front == self.rear:
#             val = self.front.data
#             self.front = None
#             self.rear = None
#         else:
#             val = self.front.data
#             self.front = self.front.next
#         return val
#
#     def peek(self):
#         if self.is_empty():
#             return
#         return self.front.data
#
#     def display(self):
#         if self.is_empty():
#             return
#         current_node = self.front
#         while current_node:
#             print(current_node.data,end=' -> ' if current_node.next else '')
#             current_node = current_node.next
#         print()
#         return
#
#
#
# class StackUsingQueue:
#
#     def __init__(self):
#         self.queue1 = Queue()
#         self.queue2 = Queue()
#
#     def is_empty(self):
#         if self.queue1.is_empty() and self.queue2.is_empty():
#             print('there is no data')
#             return True
#         else:
#             return False
#
#     def push(self,data):
#         self.queue2.enqueue(data)
#         while self.queue1.is_empty() is False:
#             self.queue2.enqueue(self.queue1.dequeue())
#         self.queue1, self.queue2 = self.queue2, self.queue1
#
#     def pop(self):
#         if self.is_empty():
#             return
#         return self.queue1.dequeue()
#
#     def peek(self):
#         if self.is_empty():
#             return
#         self.queue1.peek()
#
#     def display(self):
#         if self.is_empty():
#             return
#         self.queue1.display()
#
#
# #
# #
# # queue = StackUsingQueue()
# # queue.push(1)
# # queue.push(2)
# # queue.push(3)
# # queue.display()
# # print(queue.peek())
# # print(queue.pop())
# # queue.display()
# #
# # class QueueUsingStack:
# #
# #     def __init__(self):
# #         self.stack1 = Stack()
# #         self.stack2 = Stack()
# #
# #     def is_empty(self):
# #         if self.stack1.is_empty() and self.stack2.is_empty():
# #             print('there is no data')
# #             return True
# #         else:
# #             return False
# #
# #     def enqueue(self,data):
# #         self.stack1.push(data)
# #
# #     def dequeue(self):
# #         if self.stack2.is_empty():
# #             while self.stack1.is_empty() is False:
# #                 self.stack2.push(self.stack1.pop())
# #         return self.stack2.pop()
# #
# #     def peek(self):
# #         if self.stack2.is_empty():
# #             while self.stack1.is_empty() is False:
# #                 self.stack2.push(self.stack1.pop())
# #         return self.stack2.peek()
# #
# #     def display(self):
# #         while self.stack1.is_empty() is False:
# #             self.stack2.push(self.stack1.pop())
# #         self.stack2.display()
# #
# #
# # queue = QueueUsingStack()
# # queue.display()
# # queue.enqueue(1)
# # queue.enqueue(2)
# # queue.enqueue(3)
# # queue.display()
# # print(queue.peek())
# # print(queue.dequeue())
# # queue.display()
#
#
# class HashTable:
#
#     def __init__(self,size = 10):
#         self.size = size
#         self.table = [[] for _ in range(self.size)]
#
#     def _hash(self,key):
#         return hash(key) % self.size
#
#     def push(self,key,data):
#
#         index = self._hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 print('dupilicate key found')
#                 return
#
#         self.table[index].append([key,data])
#
#     def pop(self,key):
#         index = self._hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 val = pair[1]
#                 self.table[index].remove(pair)
#                 return val
#         return "No key found"
#
#     def search(self,key):
#         index = self._hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return "No key found"
#
# ha = HashTable()
#
# print(ha.search('sre'))
#
# ha.push('sre','sreyas')
# ha.push('np','nip')
# print(ha.search('np'))
# print(ha.pop('np'))
# print(ha.search('np'))
# print(ha.search('sre'))


#
# def qucik_sort(array):
#
#     start = 0
#     end = len(array) - 1
#     helper(array,start,end)
#


# def helper(array,start,end):
#
#     if start > end:
#         return
#     pivot = start
#     left = start+1
#     right = end
#     while left <= right:
#         if array[left] > array[pivot] and array[right] < array[pivot]:
#             array[left], array[right] = array[right] , array[left]
#         if array[left] <= array[pivot]:
#             left +=1
#         if array[right] >= array[pivot]:
#             right -= 1
#     array[right], array[pivot] = array[pivot], array[right]
#     helper(array,start,right - 1)
#     helper(array,right+1,end)
#     return array
#
# class Node:
#      def __init__(self,data):
#          self.data = data
#          self.next = None
#
#
#
# class Stack:
#
#     def __init__(self):
#         self.top = None
#         self.val = ''
#
#     def push(self,data):
#         node = Node(data)
#         if self.top:
#             node.next= self.top
#         self.top = node
#
#
#     def pop(self):
#
#         if self.top:
#             val = self.top.data
#             self.top = self.top.next
#             return val
#
# s = Stack()
# s.push('s')
# s.push('r')
# s.push('e')
# v = ''
# v += s.pop()
# v += s.pop()
# v += s.pop()
# print(v)
#

# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None
#
# class BinaryTree:
#
#     def __init__(self):
#         self.root = None
#
#     def insert(self,data):
#
#         node = Node(data)
#         current_node = self.root
#         if self.root is None:
#             self.root = node
#             return
#         while True:
#             if current_node.data > data:
#                 if current_node.left is None:
#                     current_node.left = node
#                     return
#                 else:
#                     current_node = current_node.left
#             else:
#                 if current_node.right is None:
#                     current_node.right = node
#                     return
#                 else:
#                     current_node = current_node.right
#
#     def _insert(self,node,root):
#
#         if root.data > node.data:
#             if root.left is None:
#                 root.left = node
#             else:
#                 self._insert(node,root.left)
#         else:
#             if root.right is None:
#                 root.right = node
#             else:
#                 self._insert(node,root.right)
#
#     def delete(self,data):
#
#         self.helper_delete(self.root,None,data)
#
#     def helper_delete(self,current_node,parrent_node,data):
#
#         while current_node:
#             if current_node.data > data:
#                 parrent_node = current_node
#                 current_node = current_node.left
#             elif current_node.data < data:
#                 parrent_node = current_node
#                 current_node = current_node.right
#             else:
#                 if current_node.left is not None and current_node.right is not None:
#                     current_node.data = self.get_min_value(current_node.right)
#                     self.helper_delete(current_node.right,current_node,current_node.data)
#                 else:
#                     if parrent_node is None:
#                         if current_node.left is None:
#                             self.root = current_node.right
#                         else:
#                             self.root = current_node.left
#                     else:
#                         if parrent_node.right == current_node:
#                             if current_node.left is None:
#                                 parrent_node.right = current_node.right
#                             else:
#                                 parrent_node.right = current_node.left
#                         else:
#                             if current_node.left is None:
#                                 parrent_node.left = current_node.right
#                             else:
#                                 parrent_node.left = current_node.left
#                     break
#
#     def get_min_value(self,root):
#
#         if root.left is None:
#             return root
#         else:
#             self.get_min_value(root.left)
#
#     def search(self,data):
#         current_node = self.root
#         while current_node:
#             if current_node.data > data:
#                 current_node = current_node.left
#             elif current_node.data < data:
#                 current_node = current_node.right
#             else:
#                 print('data found')
#                 return current_node.data
#
#         print('no data found')
#         return False
#
#     def in_order(self):
#         self.in_order_helper(self.root)
#         print()
#
#     def in_order_helper(self,node):
#         if node:
#             self.in_order_helper(node.left)
#             print(node.data,end=' ')
#             self.in_order_helper(node.right)
#
#     def pre_order(self):
#         self.pre_order_helper(self.root)
#         print()
#
#     def pre_order_helper(self,node):
#
#         if node:
#             print(node.data,end=' ')
#             self.pre_order_helper(node.left)
#             self.pre_order_helper(node.right)
#
#     def post_order(self):
#         self.post_order_helper(self.root)
#         print()
#     def post_order_helper(self,node):
#         if node:
#             self.post_order_helper(node.left)
#             self.post_order_helper(node.right)
#             print(node.data,end=' ')
#
#
#
#
# btree = BinaryTree()
#
# btree.insert(10)
# btree.insert(5)
# btree.insert(15)
# btree.insert(3)
# btree.insert(9)
# btree.insert(2)
# btree.insert(7)
# btree.insert(6)
# btree.insert(8)
# btree.insert(13)
# btree.insert(17)
# btree.insert(16)
# btree.insert(18)
# btree.insert(12)
# btree.insert(14)
# btree.in_order()
# btree.pre_order()
# btree.post_order()

#
#
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None
#
#
# class BinarySearchTree:
#
#     def __init__(self):
#         self.root = None
#
#     def insert(self,data):
#
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert(Node(data),self.root)
#
#     def _insert(self,node,current_node):
#
#         if node.data < current_node.data:
#             if current_node.left is None:
#                 current_node.left = node
#             else:
#                 self._insert(node,current_node.left)
#         else:
#             if current_node.right is None:
#                 current_node.right = node
#             else:
#                 self._insert(node,current_node.right)
#
#     def remove(self,data):
#         self.remove_helper(self.root,None,data)
#
#     def remove_helper(self,current_node,parrent_node,data):
#
#         while current_node:
#
#             if current_node.data > data:
#                 parrent_node = current_node
#                 current_node = current_node.left
#                 self.remove_helper(current_node,parrent_node,data)
#             elif current_node.data < data:
#                 parrent_node = current_node
#                 current_node = current_node.right
#                 self.remove_helper(current_node,parrent_node,data)
#             else:
#                 if current_node.left is not None and current_node.right is not None:
#                     current_node.data = self.get_min_val(current_node.right)
#                     self.remove_helper(current_node.right,current_node,current_node.data)
#                 else:
#                     if parrent_node is None:
#                         val = current_node.data
#                         if current_node.right is None:
#                             self.root = current_node.left
#                         else:
#                             self.root = current_node.right
#                         return val
#                     else:
#                         val = current_node.data
#                         if parrent_node.left == current_node:
#                             if current_node.right is None:
#                                 parrent_node.left = current_node.left
#                             else:
#                                 parrent_node.left = current_node.right
#                         else:
#                             if current_node.left is None:
#                                 parrent_node.right = current_node.right
#                             else:
#                                 parrent_node.right = current_node.left
#                 break
#
#
#     def get_min_val(self,root):
#         if root.left is None:
#             return root.data
#         else:
#             self.get_min_val(root.left)
#
#
#     def in_order(self):
#         val = []
#         self._in_order(self.root,val)
#         return val
#
#     def _in_order(self,node,val):
#         if node:
#             self._in_order(node.left,val)
#             val.append(node.data)
#             self._in_order(node.right,val)
#
#
# binarytree = BinarySearchTree()
# binarytree.insert(10)
# binarytree.insert(8)
# binarytree.insert(11)
# binarytree.insert(4)
# binarytree.insert(9)
# binarytree.in_order()
# binarytree.remove(0)
# print(binarytree.in_order())

#
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#
# class BinarySearchTree:
#
#     def __init__(self):
#         self.root = None
#
#     def insert(self,data):
#         if self.root is None:
#             self.root = Node(data)
#             return
#         self._insert(Node(data),self.root)
#
#     def _insert(self, node,root):
#         if root:
#             if node.data < root.data:
#                 if root.left is None:
#                     root.left = node
#                     return
#                 else:
#                     self._insert(node,root.left)
#             else:
#                 if root.right is None:
#                     root.right = node
#                     return
#                 else:
#                     self._insert(node,root.right)
#
#     def in_order(self):
#         self._in_order(self.root)
#         print()
#
#     def _in_order(self,node):
#         if node:
#             self._in_order(node.left)
#             print(node.data,end=' ')
#             self._in_order(node.right)
#
#     def remove(self,data):
#         self.delete(data,self.root,None)
#
#     def delete(self,data,current_node, parrent_node):
#
#         while current_node:
#             if data < current_node.data:
#                 parrent_node = current_node
#                 current_node = current_node.left
#                 self.delete(data,current_node,parrent_node)
#             elif data > current_node.data:
#                 parrent_node = current_node
#                 current_node = current_node.right
#                 self.delete(data,current_node,parrent_node)
#             else:
#                 if current_node.left and current_node.right:
#                     current_node.data = self.get_min_val(current_node.right)
#                     self.delete(current_node.data,current_node.right,current_node)
#                 else:
#                     if parrent_node is None:
#                         if current_node.right is None:
#                             self.root = current_node.left
#                         else:
#                             self.root = current_node.right
#                     else:
#                         if parrent_node.right == current_node:
# #                             if current_node.right is None:
# #                                 parrent_node.right = current_node.left
# #                             else:
# #                                 parrent_node.right = current_node.right
# #                         else:
# #                             if current_node.right is None:
# #                                 parrent_node.left = current_node.left
# #                             else:
# #                                 parrent_node.left = current_node.right
# #
# #
# # st = BinarySearchTree()
# #
# # st.insert(10)
# # st.insert(8)
# # st.insert(11)
# # st.insert(5)
# # st.insert(4)
# # st.insert(6)
# # st.in_order()
#
#
# # class MinHeap:
# #
# #     def __init__(self):
# #         self.heap = []
# #
# #     def build_heap(self,array):
# #         self.heap = array
# #         for i in range(self.__parent(len(self.heap)-1),-1,-1):
# #             self.__shift_down(i)
# #
# #     def insert(self,data):
# #         self.heap.append(data)
# #         self.__shift_up(len(self.heap) - 1)
# #
# #
# #     def __shift_down(self,current_index):
# #         end_index = len(self.heap) - 1
# #         left_index = self.__left_child(current_index)
# #         while left_index <= end_index:
# #             shift_index = -1
# #             right_index = self.__right_child(current_index)
# #             if right_index <= end_index and self.heap[right_index] < self.heap[left_index]:
# #                 shift_index = right_index
# #             else:
# #                 shift_index = left_index
# #             if self.heap[current_index] > self.heap[shift_index]:
# #                 self.heap[current_index],self.heap[shift_index] = self.heap[shift_index],self.heap[current_index]
# #                 current_index = shift_index
# #                 left_index = self.__left_child(current_index)
# #             else:
# #                 return
# #
# #     def __shift_up(self,current_index):
# #         parrent_index = self.__parent(current_index)
# #         while current_index > 0 and self.heap[parrent_index] > self.heap[current_index]:
# #             self.heap[parrent_index], self.heap[current_index] = self.heap[current_index], self.heap[parrent_index]
# #             current_index = parrent_index
# #             parrent_index = self.__parent(current_index)
# #
# #     def display(self):
# #         for i in self.heap:
# #             print(i,end=' | ')
# #         print()
# #     def __left_child(self,index):
# #         return (index * 2) + 1
# #
# #     def __right_child(self,index):
# #         return (index * 2) + 2
# #
# #     def __parent(self,index):
# #         return int((index - 1) / 2)
# #
# #
# # minh = MinHeap()
# # print('min heap is this:',end=' ')
# # minh.build_heap([32,44,8,16,27,18,12,10])
# # minh.display()
# #
# class MaxHeap:
#
#     def __init__(self):
#         self.heap = []
#
#     def build_heap(self, array):
#         self.heap = array
#         for i in range(self.__parent(len(self.heap) - 1), -1, -1):
#             self.__shift_down(i)
#
#     def insert(self, data):
#         self.heap.append(data)
#         self.__shift_up(len(self.heap) - 1)
#
#     def display(self):
#         for i in self.heap:
#             print(i, end=' | ')
#         print()
#
#     def __shift_down(self, current_index, end_index=None):
#         if end_index is None:
#             end_index = len(self.heap) - 1
#         left_index = self.__left_child(current_index)
#         while left_index <= end_index:
#             shift_index = -1
#             right_index = self.__right_child(current_index)
#             if right_index <= end_index and self.heap[right_index] > self.heap[left_index]:
#                 shift_index = right_index
#             else:
#                 shift_index = left_index
#             if self.heap[shift_index] > self.heap[current_index]:
#                 self.__swap(current_index, shift_index)
#                 current_index = shift_index
#                 left_index = self.__left_child(current_index)
#             else:
#                 return
#
#     def __shift_up(self, current_index):
#         parrent_index = self.__parent(current_index)
#         while current_index > 0 and self.heap[parrent_index] < self.heap[current_index]:
#             self.__swap(current_index, parrent_index)
#             current_index = parrent_index
#             parrent_index = self.__parent(current_index)
#
#     def __parent(self, current_index):
#         return int((current_index - 1) / 2)
#
#     def __left_child(self, index):
#         return (index * 2) + 1
#
#     def __right_child(self, index):
#         return (index * 2) + 2
#
#     def __swap(self, pos1, pos2):
#         self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]
#         return
#
#     def heap_sort(self):
#         self.build_heap(self.heap)
#         for i in range(len(self.heap) - 1, 0, -1):
#             self.__swap(0, i)
#             self.__shift_down(0, i - 1)
#
#
# me = MaxHeap()
# me.build_heap([32, 44, 8, 16, 27, 18, 12, 10])
# me.display()
# me.insert(33)
# me.display()
# me.insert(1)
# me.insert(2)
# me.insert(37)
# print('this is max heap:', end=' ')
# me.display()
# me.heap_sort()
# print('this is max heap:', end=' ')
# me.display()
#
#
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None
#
#
# class BinarySearchTree:
#
#     def __init__(self):
#         self.root = None
#
#     def insert(self,data):
#
#         node = Node(data)
#         current_node = self.root
#         if self.root is None:
#             self.root = node
#             return
#         while True:
#             if node.data < current_node.data:
#                 if current_node.left is None:
#                     current_node.left = node
#                     return
#                 else:
#                     current_node = current_node.left
#             else:
#                 if current_node.right is None:
#                     current_node.right = node
#                     return
#                 else:
#                     current_node = current_node.right
#
#     def search(self,data):
#
#         current_node = self.root
#         while current_node:
#             if current_node.data == data:
#                 return True
#             elif current_node.data > data:
#                 current_node = current_node.left
#             else:
#                 current_node = current_node.right
#         return False
#
#
#     def delete(self,data):
#         self.delete_helper(self.root,None,data)
#
#     def delete_helper(self,current_node,parrent_node,data):
#
#         while current_node:
#             if data < current_node.data:
#                 parrent_node = current_node
#                 current_node = current_node.left
#             elif data > current_node.data:
#                 parrent_node = current_node
#                 current_node = current_node.right
#             else:
#                 if current_node.left != None and current_node.right != None:
#                     current_node.data = self.get_min_value(current_node.right)
#                     self.delete(current_node.right,current_node,current_node.data)
#                 else:
#                     if parrent_node is None:
#                         if current_node.right is None:
#                             self.root = current_node.left
#                         else:
#                             self.root = current_node.right
#                     else:
#                         if parrent_node.left == current_node:
#                             if current_node.right is None:
#                                 parrent_node.left = current_node.left
#                             else:
#                                 parrent_node.left = current_node.right
#                         else:
#                             if current_node.right is None:
#                                 parrent_node.right = current_node.left
#                             else:
#                                 parrent_node.right = current_node.right
#                     break
#
#     def get_min_value(self,node):
#         if node.left is None:
#             return node.data
#         else:
#             self.get_min_value(node.left)
#
#     def in_order(self):
#         self.in_order_he(self.root)
#
#     def in_order_he(self,node):
#         if node:
#             self.in_order_he(node.left)
#             print(node.data,end=' ')
#             self.in_order_he(node.right)
#
#     def is_bst(self,node,min_val=float('-inf'),max_val=float('inf')):
#
#         if node is None:
#             return True
#         if node.data <= min_val or node.data >= max_val:
#             return False
#         self.is_bst(node.left,min_val,node.val)
#         self.is_bst(node.right,node.data,max_val)
#
#
# class MinHeap:
#
#     def __init__(self):
#         self.children = []
#
#     def build_heap(self,array):
#         self.children = array
#         for i in range(len(self.children) - 1,-1,-1):
#             self.shift_down(i)
#
#     def shift_down(self,current_idx):
#         end_idx = len(self.root) - 1
#         left_idx = self.left_child(current_idx)
#         while left_idx <= end_idx:
#             shif_idx = None
#             right_idx = self.right_child(current_idx)
#             if right_idx <= end_idx and self.children[right_idx] < self.children[left_idx]:
#                 shif_idx = right_idx
#             else:
#                 shif_idx = left_idx
#             if self.children[current_idx] > self.children[shif_idx]:
#                 self.heap[current_idx], self.heap[shif_idx] = self.heap[shif_idx], self.heap[current_idx]
#                 current_idx = shif_idx
#                 self.left_idx = self.left_child(current_idx)
#             else:
#                 return
#
#     def shift_up(self,current_idx):
#         parrent = self.parent(current_idx)
#         while current_idx > 0 and self.children[parrent] > self.children[current_idx]:
#             self.children[parrent], self.children[current_idx] = self.children[current_idx], self.children[parrent]
#             current_idx = parrent
#             parrent = self.parent(current_idx)
#
#     def delete(self):
#         self.children[0] , self.children[len(self.children)-1] = self.children[len(self.children)-1], self.children[0]
#         self.children.pop()
#         self.shift_down(0)
#
#     def insert(self,data):
#         self.children.append(data)
#         self.shift_up(len(self.children) - 1)
#
#     def left_child(self,index):
#         return (index*2) + 1
#
#     def right_child(self,index):
#         return (index*2) + 2
#
#     def parent(self,index):
#         return int((index - 1) / 2)
#
#
# class TrieNode:
#
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
#
#
# class PrefixTrie:
#
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self,word):
#         node = self.root
#
#         for ch in word:
#             if ch not in node.children:
#                 node.children[ch] = TrieNode()
#             node = node.children[ch]
#         node.is_end = True
#


class Node:

    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        node = Node(data)
        current_node = self.root
        if self.root is None:
            self.root = node
            return
        while current_node:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = node
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = node
                else:
                    current_node = current_node.right


bin = BinarySearchTree()



class preifix:

    def __int__(self):
        self.root = {}


    def long(self):

        current_node = self.root


class Heap:

    def __int__(self):
        self.heap = []

    def delete(self):

        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1],self.heap[0]
        self.heap.pop(0)
        self.shif_down(0)


def dfs(graph,start, visited = None):

    if visited is None:
        visited = set()

    ar = [start]
    visited.add(start)
    print(start, end=' ')
    while ar:
        val = ar.pop(0)
        for edge in graph.get(val,[]):
            if edge not in visited:
                visited.add(start)
                ar.append(start)



