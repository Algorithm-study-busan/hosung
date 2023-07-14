MAX = 100000
MOD = 1_000_000_007
dp = [0 for _ in range(MAX+1)]

dp_accumulated_mod = [0 for _ in range(3)]

def solution(n):
    global dp
    dp[1] = 1
    dp_accumulated_mod[1] = dp[1]
    dp[2] = 3
    dp_accumulated_mod[2] = dp[2]
    dp[3] = 10
    dp_accumulated_mod[0] = dp[3]
    
    dp[4] = 23
    dp[5] = 62
    dp[6] = 170

    for i in range(7, n+1) :
        dp[i] = dp[i-1] + 2*dp[i-2] + 5*dp[i-3]
        dp[i] %= MOD
        
        
        mul = [2,2,2]
        mul[i % 3] = 4
        
        for k in range(3) :
            dp[i] += dp_accumulated_mod[k] * mul[k]
            dp[i] %= MOD
        
            
            
        if i % 3 == 1 or i % 3 == 2:
            dp[i] +=2 
        else :
            dp[i] +=4
        
        dp_accumulated_mod[i%3] += dp[i-3]
        
    return dp[n]

print(solution(7))
print(solution(8))
print(solution(9))