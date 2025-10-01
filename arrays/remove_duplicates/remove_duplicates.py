from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        i = 1

        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k

sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 2, 3, 4]))
print(sol.removeDuplicates([1,1,2]))
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))