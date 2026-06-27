from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isLeaf(self, node: Optional[TreeNode]):
        if node and not node.left and not node.right:
            return True
        return False
    
    def traverse(self, node: Optional[TreeNode], depth: int):
        if not node:
            return depth
        print(node.val)

        left = node.left
        right = node.right


        left_depth = self.traverse(left, depth+1)
        right_depth = self.traverse(right, depth+1)
        return max(left_depth, right_depth)


        
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)

one.left = two
one.right = three
three.left = four

sol = Solution()
print(sol.maxDepth(one))