nums = [1,2,3,1]

dp = [0] * len(nums)

dp[0] = nums[0]

for i in range(1, len(nums)):
    dp[i] = max(dp[i-1], dp[i-2] + nums[i] if i >= 2 else nums[i])

print(max(dp))