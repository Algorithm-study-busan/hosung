import sys
sys.setrecursionlimit(100000000)

def solution(strs, t):
    word_set = set()
    for s in strs :
        word_set.add(s)
    
    dp = [-1 for _ in range(len(t))]
    
    def find_dp(idx) :
        if idx == -1 : return 0
        
        if dp[idx] != -1 : 
            return dp[idx]
        
        dp[idx] = 987654321
        for i in range(max(0,idx-4), idx+1) :
            if t[i:idx+1] in word_set :
                dp[idx] = min(dp[idx], find_dp(i-1) + 1)
        
        return dp[idx]
    
    ans = find_dp(len(t)-1)
    if ans >= 987654321 :
        return -1
    return ans
            