class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = -1
        curr_depth = 0
        for char in s:
            if char == "(":
                curr_depth += 1
                stack.append("(")
            elif char == ")":
                curr_depth -= 1
                stack.pop()
            max_depth = max(max_depth, curr_depth)
        return max_depth
