import sys

N = int(input())

work_cost = []
move_cost = []

for _ in range(N-1) :
    a,b,c,d = map(int, input().split())
    work_cost.append([a,b])
    move_cost.append([c,d])

a,b = map(int,input().split())
work_cost.append([a,b])

dp = [[-1,-1] for _ in range(N)]

def find_dp(n, k) :
    if dp[n][k] != -1 : return dp[n][k]
    if n == 0 : 
        return work_cost[0][k]
    if k == 0 :
        dp[n][k] = work_cost[n][k] + min(find_dp(n-1, k), move_cost[n-1][k+1] + find_dp(n-1, k+1))
    else :
        dp[n][k] = work_cost[n][k] + min(find_dp(n-1, k), move_cost[n-1][k-1] + find_dp(n-1, k-1))

    return dp[n][k]

print(min(find_dp(N-1, 0), find_dp(N-1, 1)))