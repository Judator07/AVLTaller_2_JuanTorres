import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.right) - getHeight(node.left)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node  

        updateHeight(node)
        balance = getBalance(node)

        if balance > 1 and getBalance(node.right) >= 0:
            return rotate_left(node)
        if balance > 1 and getBalance(node.right) < 0:
            node.right = rotate_right(node.right)
            return rotate_left(node)

        if balance < -1 and getBalance(node.left) <= 0:
            return rotate_right(node)
        if balance < -1 and getBalance(node.left) > 0:
            node.left = rotate_left(node.left)
            return rotate_right(node)

        return node

    def delete(self, val, Node):
        if Node is None:
            return Node
        elif val < Node.value:
            Node.left = self.delete(val, Node.left)
        elif val > Node.value:
            Node.right = self.delete(val, Node.right)
        else:
            if Node.left is None:
                return Node.right
            elif Node.right is None:
                return Node.left
            rgt = self.MinimumValueNode(Node.right)
            Node.value = rgt.value
            Node.right = self.delete(rgt.value, Node.right)

        Node.height = 1 + max(getHeight(Node.left), getHeight(Node.right))
        balance = getBalance(Node)

        if balance > 1 and getBalance(Node.right) >= 0:
            return rotate_left(Node)
        if balance > 1 and getBalance(Node.right) < 0:
            Node.right = rotate_right(Node.right)
            return rotate_left(Node)

        if balance < -1 and getBalance(Node.left) <= 0:
            return rotate_right(Node)
        if balance < -1 and getBalance(Node.left) > 0:
            Node.left = rotate_left(Node.left)
            return rotate_right(Node)

        return Node

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def MinimumValueNode(self, Node):
        if Node is None or Node.left is None:
            return Node
        else:
            return self.MinimumValueNode(Node.left)

avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")
avl.inorder(avl.root)
print("")

avl.delete(20, avl.root)
avl.inorder(avl.root)
print("")
avl2 = AVLTree()
values_to_insert2 = [10, 30, 22, 40, 51, 25, 7, 92]
for val in values_to_insert2:
    avl2.insert(val)
avl.inorder(avl2.root)
print("****************")
print("")
print("")

for val in [10, 30, 22, 40, 51, 25, 7, 92]:
    avl2.root = avl2.delete(val, avl2.root)
avl.inorder(avl2.root)