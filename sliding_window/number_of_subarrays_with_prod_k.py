
def sol(nums, k):
    start = 0
    curr_product = 1
    num_of_subarray = 0
    end = 0

    if k <= 1:
        return 0

    while end < len(nums):
        curr_product *= nums[end]

        while curr_product >= k:
            curr_product = curr_product // nums[start]
            start += 1
        num_of_subarray += (end - start) + 1
        end += 1

    return num_of_subarray
