from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    balanced = True

    def traverse(self, curr_node):
        if not curr_node:
            return 0
        
        left = curr_node.left
        right = curr_node.right

        print(f"Curr Node: {curr_node.val}")

        left_height = self.traverse(left)
        right_height = self.traverse(right)

        print(f"Curr node: {curr_node.val} Height: {max(left_height, right_height) + 1}")

        if (abs(left_height - right_height)) > 1:
            self.balanced = False

        return max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]):
        self.traverse(root)
        return self.balanced

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)

one.left = two
one.right = three
three.left = four

sol = Solution()
sol.isBalanced(one)
