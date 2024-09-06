INF = 987654321
MIN = 0
MAX = 1

def solution(arr):
    N = len(arr)
    dp = [[[INF for _ in range(2)] for _ in range(N)] for _ in range(N)]
    
    def find_dp(s, e, k) :
        if dp[s][e][k] != INF : return dp[s][e][k]
        if s == e : return int(arr[s])
        
        if k == MAX : dp[s][e][k] = -INF
        else : dp[s][e][k] = INF
        
        for i in range(s+1, e, 2) :
            if k == MAX :
                if arr[i] == '+' :
                    dp[s][e][k] = max(dp[s][e][k], find_dp(s,i-1,MAX) + find_dp(i+1, e, MAX))
                else : 
                    dp[s][e][k] = max(dp[s][e][k], find_dp(s,i-1,MAX) - find_dp(i+1,e,MIN))
            else :
                if arr[i] == '+' :
                    dp[s][e][k] = min(dp[s][e][k], find_dp(s, i-1, MIN) + find_dp(i+1,e,MIN))
                else :
                    dp[s][e][k] = min(dp[s][e][k], find_dp(s,i-1,MIN) - find_dp(i+1,e,MAX))
        
        return dp[s][e][k]
            
    return find_dp(0, N-1, MAX)