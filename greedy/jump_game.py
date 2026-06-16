nums = [2,0,1,0,4]


def sol_1(nums):
    last_index = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= last_index:
            last_index = i
    
    return True if last_index == 0 else False





