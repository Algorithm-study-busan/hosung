def solution(n):
    dp = [1, 1, 2]
    
    for i in range(3, n+1) :
        tmp = 0
        
        for j in range(i) :
            tmp += dp[j] * dp[i-1-j]
            
        dp.append(tmp)
        
    
    return dp[n]