class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def preorder(root: Node):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def postorder(root: Node):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('Прямий обхід')
preorder(root)

print('Центровий обхід')
inorder(root)

print('Зворотний обхід')
postorder(root)
