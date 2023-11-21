from show_tree import draw_tree


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    # if key == root.val:
    #     return root
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or key == root.val:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def min_value_node(root):
    current = root
    while current.left:
        current = current.left
    return current


def delete(root, key):
    if not root:
        return root

    # if root.left is not None and key == root.left.val:
    #     if (root.left.left is None) and (root.left.right is None):
    #         root.left = None
    #         return root
    #
    # if root.right is not None and key == root.right.val:
    #     if (root.right.left is None) and (root.right.right is None):
    #         root.right = None
    #         return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp_root = root.right
            root = None
            return temp_root
        elif not root.right:
            temp_root = root.left
            root = None
            return temp_root
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


def postorder(root: Node):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


# Створення дерева
root = Node(5)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
# root = insert(root, 7)
root = insert(root, 8)
root = insert(root, 8.5)
root = insert(root, 1)
root = insert(root, 7.5)
root = insert(root, 7.4)
root = insert(root, 7.6)

root = insert(root, 8.4)
root = insert(root, 8.6)

r = search(root, 5)
if r:
    print(r.val)

r = search(root, 10)
if r:
    print(r.val)

# root = delete(root, 5)
draw_tree(root)
