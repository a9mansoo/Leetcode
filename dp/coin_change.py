amount = 11
coins = [1,2,5]


dp = [amount + 1] * (amount+1)
dp[0] = 0

for a in range(1, amount+1):
    for c in coins:
        if (a - c) >= 0 :
            diff = a - c
            minimum = min(1 + dp[diff], dp[a])
            dp[a] = minimum
print(dp[amount])