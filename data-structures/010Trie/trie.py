
class TrieNode:

    def __init__(self):
        self.children = {}


class Trie:

    def __init__(self, string):
        self.root = TrieNode()
        self.end_symbol = '*'
        self.populate_suffix_trie(string)

    def populate_suffix_trie(self,string):
        for i in range(len(string)):
            self.insert_substring_starting_at(i , string)

    def insert_substring_starting_at(self, index, string):
        node = self.root
        for i in range(index,len(string)):
            if string[i] not in node.children:
                new_node = TrieNode()
                node.children[string[i]] = new_node

            node = node.children[string[i]]
        node.children[self.end_symbol] = None

    def contains(self, string):
        node = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True if self.end_symbol in node.children else False



trie = Trie('mannan')
print(trie.contains('annan'))

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTrie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


class SuffixTree:

    def __init__(self, string):
        self.root = TrieNode()
        self.is_word = False
        self.suffix_string(string)

    def insert(self,word):
        pass

    def suffix_string(self,string):
        for i in range(len(string)):
            self.build_suffix_string(i,string)


    def build_suffix_string(self, index,string):

        node = self.root
        for i in range(index,string):
            if string[i] not in node.children:
                node.children[string[i]] = TrieNode()
            node = node.children[string[i]]


