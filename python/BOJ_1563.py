N = int(input())

dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(1001)]
MOD = 1_000_000

dp[1][0][0] = 1
dp[1][0][1] = 1
dp[1][1][0] = 1

for n in range(2, 1001) :
    dp[n][0][0] = (dp[n-1][0][0] + dp[n-1][0][1] + dp[n-1][0][2]) % MOD
    dp[n][0][1] = dp[n-1][0][0]
    dp[n][0][2] = dp[n-1][0][1]
    dp[n][1][0] = (dp[n-1][0][0] + dp[n-1][0][1] + dp[n-1][0][2] + dp[n-1][1][0] + dp[n-1][1][1] + dp[n-1][1][2]) % MOD
    dp[n][1][1] = dp[n-1][1][0]
    dp[n][1][2] = dp[n-1][1][1]
    
ans = 0
for i in range(2) :
    for j in range(3) :
        ans += dp[N][i][j]

print(ans % MOD) 