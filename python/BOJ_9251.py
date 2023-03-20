import sys
sys.setrecursionlimit(100000)

MAX = 1000

s1 = input()
s2 = input()

dp = [[-1 for _ in range(MAX)] for _ in range(MAX)]

def find_dp(i, j) :
    if i == -1 or j == -1 : return 0
    if dp[i][j] != -1 : return dp[i][j]
    if s1[i] == s2[j] :
        dp[i][j] = 1 + find_dp(i-1,j-1)
    else :
        dp[i][j] = max(find_dp(i-1,j), find_dp(i,j-1))
        
    return dp[i][j]

print(find_dp(len(s1)-1, len(s2)-1))