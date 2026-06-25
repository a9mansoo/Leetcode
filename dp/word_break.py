s = "leetcode"
wordDict = ["leet","code"]

dp = [False] * (len(s) + 1)
dp[len(s)] = True


for i in range(len(s), -1, -1):
    for j in range(i+1, len(s) + 1):
        
        if s[i:j] in wordDict and dp[j]:
            print(s[i:j])
            dp[i] = True
            break

print(dp)