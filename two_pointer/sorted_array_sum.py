from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left, right]
            elif curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
        return []

sol = Solution()

print(sol.twoSum([2,7,11,15], 9))