import sys

sys.setrecursionlimit(1000000)

dp = [-1 for _ in range(200100)]
N = -1
tops = []
MOD = 10007 

def find_dp(n) :
    if n == N*2 or n == N*2+1 : return 1
    
    if dp[n] != -1 : return dp[n]
    
    if n % 2 == 0 :
        dp[n] = find_dp(n+1) + find_dp(n+2)
    else :
        dp[n] = find_dp(n+1) + find_dp(n+2)
        if tops[n//2] : dp[n] += find_dp(n+1)
        
    dp[n] %= MOD
    return dp[n]
        
        

def solution(n, tops_):
    global dp, N, tops
    N = n
    tops = tops_
    return find_dp(0)