from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    end_window = 0
    start_window = 0
    curr_min = 100000000000
    curr_sum = 0
    while end_window < n:
        curr_sum += nums[end_window]
        while curr_sum >= target:
            curr_min = min(curr_min, end_window - start_window + 1)
            curr_sum -= nums[start_window]
            start_window += 1
            
            
        end_window += 1
    if curr_min == 100000000000:
        return 0
    return curr_min
    




target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))
target = 4
nums = [1, 4, 5]
print(minSubArrayLen(target, nums))