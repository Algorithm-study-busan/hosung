dp = [ [-1 for _ in range(201)] for _ in range(201) ]

def find_dp(s, e, Ms) :
    if s == e : return 0
    if dp[s][e] != -1 : return dp[s][e]
    ret = 987654321
    for i in range(s, e) :
        ret = min(ret, Ms[s][0] * Ms[i][1] * Ms[e][1] + find_dp(s, i, Ms) + find_dp(i+1, e, Ms))
    dp[s][e] = ret
    return ret
    

def solution(matrix_sizes):
    return find_dp(0, len(matrix_sizes)-1, matrix_sizes)