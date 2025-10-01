from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        print(citations)
        tot = len(citations)
        max_item = -1
        i = 0
        while i < len(citations):
            papers_left = (tot - i)
            if citations[i] >= papers_left:
                max_item = max(papers_left, max_item)
            i += 1
        return max_item





sol = Solution()
print(sol.hIndex([10, 8, 5, 4, 3, 1]))
print(sol.hIndex([0, 1, 3, 5, 6]))