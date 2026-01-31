from typing import List



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_count = n // 2

        nums.sort()

        return nums[majority_count]


sol = Solution()

sol.majorityElement([2,2,1,1,1,2,2])        