from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    shift_index = length - k
    i = length - 1
    while i >= shift_index:
        nums.insert(0, nums[length - 1])
        nums.pop()
        i -= 1
    



nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)

