from typing import List



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_count = n // 2

        nums.sort()

        return nums[majority_count]
    
    def solution_2(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            
            if candidate is not None and num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


sol = Solution()

sol.majorityElement([2,2,1,1,1,2,2])        