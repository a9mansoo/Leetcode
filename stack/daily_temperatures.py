from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst_indexes = [0]* len(temperatures)
        stack = []
        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                lst_indexes[prev_index] = i - prev_index
            stack.append(i)
        return lst_indexes






sol = Solution()
print(sol.dailyTemperatures([30,38,30,36,35,40,28]))
