def solution(n, count):
    dp = [[-1 for _ in range(101)] for _ in range(101)]
    MOD = 1_000_000_007
    
    def find_dp(nn, cc) :
        if nn == n and cc == count :
            return 1
        if nn == n or cc > count:
            return 0
        
        if dp[nn][cc] != -1 : return dp[nn][cc]
    
        
        dp[nn][cc] = find_dp(nn+1, cc+1) + nn*2 * find_dp(nn+1, cc)
        dp[nn][cc] %= MOD
        return dp[nn][cc]
    
    return find_dp(1,1)