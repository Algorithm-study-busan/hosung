import sys
sys.setrecursionlimit(10000000)

N = int(input())
arr = list(map(int, input().split()))
j = int(input())
c = int(input())

dp = [[-1 for _ in range(1001)] for _ in range(1001)]
a = arr[0]
b = sum(arr[1:])

def find_dp(n, m) :
    if dp[n][m] != -1 : return dp[n][m]
    if n < 0 or m < 0 : return 0;
    if n == 0 and m == 0 : return 1
    
    dp[n][m] = (find_dp(n-1, m) * (a+j*(n-1)) / (a+j*(n-1) + b+j*m) + 
                find_dp(n, m-1) * (b+j*(m-1)) / (a+j*n + b+j*(m-1)))
    return dp[n][m]

ans = 0
for ci in range(c+1) :
    ans += find_dp(ci, c-ci) * (a+(j*ci))
    

print(ans)
    
