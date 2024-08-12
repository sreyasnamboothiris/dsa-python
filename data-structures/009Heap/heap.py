

class MinHeap:

    def __init__(self):
        self.heap = []

    def build_heap(self,array):
        self.heap = array
        for i in range(self.parent(len(self.heap)-1),-1,-1):
            self.shift_down(i)

    def shift_down(self, current_idx):
        end_idx = len(self.heap) - 1
        left_idx = self.left_child(current_idx)
        while left_idx <= end_idx:
            right_idx = self.right_child(current_idx)
            idx_shift = 0
            if right_idx <= end_idx and self.heap[right_idx] < self.heap[left_idx]:
                idx_shift = right_idx
            else:
                idx_shift = left_idx
            if self.heap[current_idx] > self.heap[idx_shift]:
                self.heap[current_idx], self.heap[idx_shift] = self.heap[idx_shift], self.heap[current_idx]
                current_idx = idx_shift
                left_idx = self.left_child(current_idx)
            else:
                return

    def shift_up(self, current_idx):
        parrent_idx = self.parent(current_idx)
        while current_idx > 0 and self.heap[current_idx] < self.heap[parrent_idx]:
            self.heap[current_idx], self.heap[parrent_idx] = self.heap[parrent_idx], self.heap[current_idx]
            current_idx = parrent_idx
            parrent_idx = self.parent(current_idx)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1],self.heap[0]
        self.heap.pop()
        self.shift_down(0)

    def insert(self,data):
        self.heap.append(data)
        self.shift_up(len(self.heap)-1)

    def left_child(self,index):
        return (index * 2) + 1

    def right_child(self,index):
        return (index * 2) + 2

    def parent(self,index):
        return int((index - 1) / 2)

    def display(self):
        print(self.heap)

minheap = MinHeap()
minheap.build_heap([32,44,8,16,27,18,12,10])
minheap.display()
minheap.insert(1)
minheap.display()
minheap.remove()
minheap.display()
print(minheap.peek())


class MaxHeap:

    def __init__(self):
        self.heap = []

    def build_heap(self,array):
        self.heap = array
        for i in range(len(self.heap)-1,-1,-1):
            self.shift_down(i)

    def shift_down(self,current_idx):
        end_idx = len(self.heap) - 1
        left_child = self.left_child(current_idx)
        while left_child <= end_idx:
            shift_idx = None
            right_child = self.right_child(current_idx)
            if right_child <= end_idx and self.heap[right_child] > self.heap[left_child]:
                shift_idx = right_child
            else:
                shift_idx = left_child
            if self.heap[shift_idx] > self.heap[current_idx]:
                self.heap[current_idx],self.heap[shift_idx] = self.heap[shift_idx], self.heap[current_idx]
                current_idx = shift_idx
                left_child = self.parent(current_idx)
            else:
                return

    def remove(self):
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        self.heap.pop()
        self.shift_down(0)

    def insert(self,data):
        self.heap.append(data)
        self.shift_up(len(self.heap) - 1)

    def shift_up(self,current_idx):
        parent_idx = self.parent(current_idx)
        while current_idx > 0 and self.heap[parent_idx] < self.heap[current_idx]:
            self.heap[current_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[current_idx]
            current_idx = parent_idx
            parent_idx = self.parent(current_idx)

    def sort(self,array):
        self.build_heap(array)
        for i in range(len(self.heap) - 1, 0 ,-1):
            self.heap[i],self.heap[0] = self.heap[0],self.heap[i]
            self.shift_down(i)

    def left_child(self,index):
        return (index * 2) + 1

    def right_child(self,index):
        return (index * 2) + 2

    def parent(self,index):
        return int((index - 1)/2)



