nums = []

dp = [1] * len(nums)
dp[0] = 1

for i in range(len(nums)):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(1 + dp[j], dp[i])
print(dp)
print(max(dp))