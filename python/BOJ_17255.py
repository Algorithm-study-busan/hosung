dp = dict()

N = input()

def find_dp(s) :
    if len(s) == 1 : return 1
    if s in dp : return dp[s]
    
    dp[s] = 0
    ls = s[1:]
    rs = s[:-1]
    if ls == rs : 
        dp[s] = find_dp(ls)
    else :
        dp[s] = find_dp(ls) + find_dp(rs)
    
    return dp[s]

print(find_dp(N))