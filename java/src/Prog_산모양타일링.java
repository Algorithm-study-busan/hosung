class Solution {
    public int MOD = 10007;
    
    public int solution(int n, int[] tops) {
        int[] dp = new int[200001];
        
        dp[0] = 1;
        if (tops[0] == 1) dp[1] = 3;
        else dp[1] = 2;
        
        for (int i=2;i<=2*n;i++) {
            if (i%2 == 1 && tops[i/2] == 1) dp[i] = (dp[i-1]*2 + dp[i-2]) % MOD;
            else dp[i] = (dp[i-1] + dp[i-2]) % MOD;
        }
        
        return dp[2*n];
    }
    
    
}