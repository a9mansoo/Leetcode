m = 3
n = 7


cols = n
rows = m
dp = [[0] * cols for i in range(m)]
print(dp)
# First row is all ones
dp[0] = [1] * n

# First columns is all ones
for j in range(rows):
    dp[j][0] = 1

for r in range(1, rows):
    for c in range(1, cols):

        dp[r][c] = dp[r-1][c] + dp[r][c-1]

print(dp[m-1][n-1])
