S = input()
M = int(input())
score = dict()
for _ in range(M) :
    a,b = input().split()
    if a in score :
        score[a] = max(score[a], int(b))
    else :
        score[a] = int(b)
    
dp = [[-1 for _ in range(1000)] for _ in range(1000)]
    
def find_dp(s, e) :
    if e == len(S) :
        return e-s
    if dp[s][e] != -1 : return dp[s][e]
    
    dp[s][e] = max(1 + find_dp(s+1, e+1), find_dp(s, e+1))
    if S[s:e+1] in score :
        dp[s][e] = max(dp[s][e], score[S[s:e+1]] + find_dp(e+1, e+1))
    return dp[s][e]

print(find_dp(0, 0))
    