from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    q = deque()

    q.append(root)

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if not node:
                continue
            print(node.val)
            left = node.left
            right = node.right

            q.append(left)
            q.append(right)


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)

one.left = two
one.right = three
three.left = four

bfs(one)