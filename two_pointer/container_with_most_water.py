from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            min_height = min(height[left], height[right])
            base = right - left
            curr_area = min_height*base

            max_area = max(max_area, curr_area)

            # So if the left height is not good, 
            # we will increment since it's the limiting factor
            # if right is the limiting height, we decrement that
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))