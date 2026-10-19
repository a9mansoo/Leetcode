from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        nums.sort(key=lambda x: (counter[x], -x))
        return nums

