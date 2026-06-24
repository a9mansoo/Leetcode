nums = [2,0,1,0,4]


def sol_1(nums):
    last_index = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= last_index:
            last_index = i
    
    return True if last_index == 0 else False


def sol_2(nums):
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False
        
        farthest = max(farthest, i+nums[i])
    return True


def sol_3(nums):
    # dp[i] = can I reach index i?
    dp = [False] * len(nums)
    dp[0] = True

    for i in range(0, len(nums)):
        if dp[i]:
            for j in range(i+1, len(nums)):
                if (i+nums[i]) >= j:
                    dp[j] = True