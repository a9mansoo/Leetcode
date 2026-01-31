

def brute_force(nums, k):
    max_sum = -10000
    curr_index = (0, 0)

    for i in range(len(nums)):
        if (i+k) > len(nums):
            break
        curr_sum = sum(nums[i:i+k])
        if curr_sum > max_sum:
            curr_index = (i, i+k)
            max_sum = curr_sum
    return max_sum, nums[curr_index[0]:curr_index[1]]


def sliding_window(nums, k):
    curr_sum = sum(nums[:k])
    curr_max = curr_sum
    start_index = 0

    for i in range(k, len(nums)):
        curr_sum = curr_sum - nums[i-k] + nums[i]
        if curr_sum > curr_max:
            curr_max = curr_sum
            start_index = i - k + 1
    return nums[start_index:start_index+k]


print(sliding_window([2, 1, 5, 1, 3, 2], 3))
