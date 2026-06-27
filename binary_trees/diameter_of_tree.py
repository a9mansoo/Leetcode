from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0

    def traverse(self, curr_node: Optional[TreeNode]) -> int:
        if not curr_node:
            return 0
        
        left = curr_node.left
        right = curr_node.right

        print(f"Curr Node: {curr_node.val}")
        
        left_height = self.traverse(left)
        right_height = self.traverse(right)

        self.diameter = max(self.diameter, left_height + right_height)
       
        print(f"Current Node: {curr_node.val} Left Height: {left_height} Right Height: {right_height}")
        return max(left_height, right_height) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.diameter
    

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)

one.right = two
two.left = three
two.right = four
three.left = five

sol = Solution()
print(sol.diameterOfBinaryTree(one))
    
    
