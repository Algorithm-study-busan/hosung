import java.util.*;

class Solution {
    public int INF = 987654312;
    public int[][] dp = new int[110][210];
    List<List<Integer>> edges = new ArrayList<>();
    
    public int find_dp(int t, int n, int[] gps_log) {
        if (t == gps_log.length-1) {
            if (gps_log[t] == n) return 0;
            return INF;
        }
        
        if (dp[t][n] != -1) return dp[t][n];
        
        dp[t][n] = find_dp(t+1, n, gps_log);
        for (int nxt : edges.get(n)) {
            dp[t][n] = Math.min(dp[t][n], find_dp(t+1, nxt, gps_log));
        }
        
        if (n != gps_log[t]) dp[t][n]++;
        
        return dp[t][n];
    }
    
    public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {
        
        for (int i=0;i<=n;i++) {
            List<Integer> arr = new ArrayList<>();
            edges.add(arr);
        }
        
        for (int i=0;i<110;i++) {
            for (int j=0;j<210;j++) {
                dp[i][j] = -1;
            }
        }
        
        for (int[] edge : edge_list) {
            int a = edge[0];
            int b = edge[1];
            edges.get(a).add(b);
            edges.get(b).add(a);
        }
        
        int ans = find_dp(0, gps_log[0], gps_log);
        if (ans >= INF) return -1;
        return ans;
    }
}