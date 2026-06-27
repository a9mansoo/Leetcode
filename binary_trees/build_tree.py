from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr):
    queue = deque()
    root = TreeNode(arr[0], None, None)
    queue.append(root)
    i = 0
    n = len(arr)

    while queue:
        node = queue.popleft()

        if i > n:
            break
        
        if not arr[i]:
            i += 1
            continue

        if 2*i+1 < n and arr[2*i+1] is not None:
            left = TreeNode(arr[2*i+1], None, None)
            node.left = left
            queue.append(left)
        
        if 2*i+2 < n and arr[2*i+2] is not None:
            right = TreeNode(arr[2*i+2], None, None)
            node.right = right
            queue.append(right)
        i += 1
    return root

root = build_tree([1,2,3,4,None,None,None,5])