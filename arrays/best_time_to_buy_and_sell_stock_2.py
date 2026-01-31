from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0

        n = len(prices)

        index = 0
        next_index = 1

        while index < (n-1):
            curr_elem = prices[index]
            next_elem = prices[next_index]
            if (next_elem - curr_elem) > 0:
                curr_profit += (next_elem - curr_elem)
            index += 1
            next_index += 1
        
        return curr_profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([1,2,3,4,5]))
print(sol.maxProfit([7,6,4,3,1]))