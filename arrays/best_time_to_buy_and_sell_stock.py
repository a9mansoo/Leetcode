from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        curr_max = -20

        n = len(prices)
        index = 1

        while index < n:
            curr_price = prices[index]

            curr_min = min(curr_min, curr_price)
            curr_max = max(curr_max, curr_price - curr_min)
            index += 1
        
        if curr_max < 0:
            return 0
        
        return curr_max




sol = Solution()
sol.maxProfit([7,1,5,3,6,4])

sol.maxProfit([7,6,4,3,1])