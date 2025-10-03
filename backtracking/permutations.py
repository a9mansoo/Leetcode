from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [False] * len(nums)
        res = []

        def backtrack(perm, selection):
            if selection == 0:
                copy = perm[:]
                res.append(copy)
                return
            
            for i in range(len(nums)):
                if permutations[i]:
                    continue
                perm.append(nums[i])
                permutations[i] = True
                backtrack(perm, selection - 1)
                perm.pop()
                permutations[i] = False
        backtrack([], len(nums))
        return res


sol = Solution()
print(sol.permute([1,2,3]))
