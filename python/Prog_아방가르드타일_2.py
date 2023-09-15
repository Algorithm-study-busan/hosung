MAX = 100000
MOD = 1_000_000_007
dp = [0 for _ in range(MAX+1)]

def solution(n):
    global dp
    dp[1] = 1
    dp[2] = 3
    dp[3] = 10    
    dp[4] = 23
    dp[5] = 62
    dp[6] = 170
    
    for i in range(7, n+1) :
        dp[i] = dp[i-1] + dp[i-2]*2 + dp[i-3]*6 + dp[i-4] - dp[i-6]
        dp[i] %= MOD
        
    return dp[n]