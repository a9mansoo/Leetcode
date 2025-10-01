from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        i = 0
        while i < len(intervals):
            if i == 0:
                merged.append(intervals[i])
                i+= 1
                continue
            
            curr_interval = intervals[i]

            min_curr = curr_interval[0]
            max_curr = curr_interval[1]

            if len(merged) > 0:
                merged_interval = merged[-1]
                sub_min = merged_interval[0]
                sub_max = merged_interval[1]

                if min_curr <= sub_max:
                    merged[-1] = [min(min_curr, sub_min), max(sub_max, max_curr)]
                else:
                    merged.append(curr_interval)
            i+= 1
        return merged



lst = [[1,3],[2,6],[8,10],[15,18]]

sol = Solution()
print(sol.merge(lst))

