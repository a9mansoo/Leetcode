class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in range(0, len(s)):
            if not s[i].isdigit():
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
        
        new_s = ""
        while stack:
            letter = stack.pop()
            new_s = letter + new_s
        return new_s
