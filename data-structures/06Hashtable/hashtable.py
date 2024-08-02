# class HashTable:
#
#     def __init__(self, size=6):
#         self.size = size
#         self.table = [[] for _ in range(size)]
#
#     def _hash(self, key):
#         return hash(key) % self.size
#
#     def insert(self, key, value):
#         index = self._hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         self.table[index].append([key, value])
#
#     def search(self, key):
#         index = self._hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return None
#
#     def display(self):
#         for i, entry in enumerate(self.table):
#             if entry:
#                 print(f"index {i}: {entry}")
#
#
# hashtable = HashTable()
# hashtable.insert(34, 34)
# hashtable.insert('name', 'sreyas')
# hashtable.insert('age', 24)
# hashtable.insert('89', 89)
# hashtable.display()
#


class HashTable:

    def __init__(self,size = 10):
        self.size = size
        self.table = [[] for _ in range(self.size)]


    def _hash(self,key):
        index = hash(key) % self.size
        return index

    def add_element(self,key,value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print('Duplicate Key Found!!!\n error: duplicate keys are not allowed in hash table.\n Solution: if '
                      'you want to update, call update() function.\n Thank you')
                return
        self.table[index].append([key,value])

    def display(self):
        for index in range(self.size):
            if self.table[index]:
                for item in self.table[index]:
                    print('key: ',item[0],'value: ',item[1])

    def update(self,key,value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value

    def search(self,key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        print('There is no key named: ',key)
        return None

    def delete(self,key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
        print('there is no key named: ',key)
        return None


has = HashTable()
has.add_element('name','Sreyas')
has.add_element('age',24)
has.update('name','sreejesh')
has.display()
has.delete('age')
has.display()