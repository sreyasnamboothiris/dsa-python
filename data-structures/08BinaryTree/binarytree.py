class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.data = item


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        node = self.root
        if self.root is None:
            self.root = Node(data)
            return
        while True:
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(data)
                    break
                else:
                    node = node.right

    def search(self, data):

        current_node = self.root

        while current_node:

            if data < current_node.data:
                current_node = current_node.left
            elif data > current_node.data:
                current_node = current_node.right
            else:
                return True

        return False

    def delete(self, data):
        self.delete_helper(data, self.root, None)

    def delete_helper(self, data, current_node, parrent_node):

        while current_node:
            if data < current_node.data:
                parrent_node = current_node
                current_node = current_node.left
            elif data > current_node.data:
                parrent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left != None and current_node.right != None:
                    current_node.data = self.get_min_val(current_node.right)
                    self.delete_helper(current_node.data, current_node.right, current_node)
                else:
                    if parrent_node == None:
                        if current_node.right is None:
                            self.root = current_node.left
                        else:
                            self.root = current_node.right
                    else:
                        if parrent_node.left == current_node:
                            if current_node.right == None:
                                parrent_node.left = current_node.left
                            else:
                                parrent_node.left = current_node.right
                        else:
                            if current_node.right == None:
                                parrent_node.right = current_node.left
                            else:
                                parrent_node.right = current_node.right
                    break

    def get_min_val(self, current_node):
        if current_node.left == None:
            return current_node.data
        else:
            self.get_min_val(current_node.left)

    def in_order(self):
        self.in_order_helper(self.root)

    def in_order_helper(self, node):
        if node:
            self.in_order_helper(node.left)
            print(node.data, end=' ')
            self.in_order_helper(node.right)

    def pre_order(self):
        self.pre_order_helper(self.root)

    def pre_order_helper(self, node):
        if node:
            print(node.data, end=' ')
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    def post_order(self):
        self.post_order_helper(self.root)

    def post_order_helper(self, node):
        if node:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.data, end=' ')


tree = BinarySearchTree()
tree.insert(10)
tree.insert(8)
tree.insert(11)
tree.insert(4)
tree.insert(9)

# print(tree.search(11))
tree.in_order()
print()
tree.pre_order()
print()
tree.post_order()
