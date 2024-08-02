
class HashTable:

    def __init__(self, size = 10):
        self.size = size
        self.tables = [[] for _ in range(size)]

    def _hash(self, key):
        index = hash(key) % self.size
        return index

    def push(self, key, data):
        index = self._hash(key)
        for pair in self.tables[index]:
            if pair[0] == key:
                print('duplicate key found!!!')
                return
        self.tables[index].append([key,data])
        return

    def pop(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.tables[index].remove(pair)
                return
        print('there is no key named: ',key)

    def search(self, key):
        index = self._hash(key)
        for pair in self.tables[index]:
            if pair[0] == key:
                return pair[1]

        return "No key found"


k = HashTable()
k.push('name','sreyas')
k.push('age',24)
k.push('no',4)
k.push(8281,'mb')
print(k.search(8281))