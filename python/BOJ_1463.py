N = int(input())

dp = [-1 for _ in range(N+1)]
INF = 987654321

def find_dp(n) :
    if dp[n] != -1 : return dp[n]
    if n == 1 : return 0
    if n < 4 : return 1
    print(n)
    
    dp[n] = min(find_dp(n//3) + n%3+1, find_dp(n//2) + n%2+1)
    
    return dp[n]

print(find_dp(N))