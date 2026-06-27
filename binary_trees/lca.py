from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, p, q):
        if not node:
            return None

        # If p is less than the current node
        # and q is greater than the current node
        # then we have a split and the current node is the LCA
        if (p.val < node.val) and (q.val < node.val):
            return self.traverse(node.left, p, q)
        
        elif (p.val > node.val) and (q.val > node.val):
            return self.traverse(node.right, p, q)
        
        else:
            return node

        


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        return self.traverse(root, p, q)
        


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)
eight = TreeNode(8)
nine = TreeNode(9)

five.left = three
five.right = eight
three.left = one
three.right = four
one.right = two

eight.left = seven
eight.right = nine

sol = Solution()
print(sol.lowestCommonAncestor(five, four, three))