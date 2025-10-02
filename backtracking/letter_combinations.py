from typing import List



class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        num_of_digits = len(digits)

        def backtrack(index, word):
            if index == num_of_digits:
                res.append(word)
                return
            
            letters = map.get(digits[index])
            for letter in letters:
                backtrack(index+1, word + letter)
        
        backtrack(0, "")
        return res

sol = Solution()
print(sol.letterCombinations("23"))



