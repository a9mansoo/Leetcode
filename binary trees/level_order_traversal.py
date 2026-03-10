from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst_nodes = []
        q = deque()
        q.append(root)

        while q:
            sub_list = []
            for _ in range(len(q)):
                node = q.popleft()

                if not node:
                    continue

                sub_list.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if sub_list:
                lst_nodes.append(sub_list)
        return lst_nodes


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)

one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

sol = Solution()
print(sol.levelOrder(one))
