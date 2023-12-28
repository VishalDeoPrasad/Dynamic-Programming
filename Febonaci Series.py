#method -1: Memorization (top down approch)
def febo(n,dp):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = febo(n-1, dp)+febo(n-2, dp)
        return dp[n]

dp = [-1]*8  
print(febo(6, dp))

#method 2:- Tebulaion (bottoms up approch)
dp = [0]*101
dp[0] = 0
dp[1] = 1
for i in range(2, 101):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[6])

    