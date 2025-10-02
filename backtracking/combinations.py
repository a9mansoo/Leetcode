from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst_numbers = [i for i in range(1, n+1)]
        res = []

        def backtrack(num_left, lst_combos, index):
            if num_left == 0:
                copy = lst_combos[:]
                res.append(copy)
                return
            for i  in range(index, len(lst_numbers)
            ):
                lst_combos.append(lst_numbers[i])
                backtrack(num_left-1, lst_combos, i+1)
                lst_combos.pop()
        
        backtrack(k, [], 0)
        return res


sol = Solution()
print(sol.combine(4, 2))
        
