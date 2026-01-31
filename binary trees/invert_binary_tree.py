"""
   4
   / \
  2   7
 / \ / \
1  3 6  9

4
   / \
  7   2
 / \ / \
9  6 3  1
"""


def invert_tree(node):
    if node is None:
        return None
    
    temp = node.right
    node.right = node.left
    node.left = temp

    invert_tree(node.left)
    invert_tree(node.right)

    return node


class Node:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

root_left = Node("2", None, None)
root_right = Node("3", None, None)
root = Node("4", root_left, root_right)

invert_tree(root)