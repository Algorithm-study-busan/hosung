class Solution {
    public int[][][] visited = new int[101][101][20000];
    
    public int move(int sr, int sc, int er, int ec, int cnt) {
        while (sr != er) {
            visited[sr][sc][cnt]++;
            cnt += 1;
            
            if (sr > er) sr -= 1;
            else sr += 1;
        }
        
        while (sc != ec) {
            visited[sr][sc][cnt]++;
            cnt += 1;
            if (sc > ec) sc -= 1;
            else sc += 1;
        }
        return cnt;
    }
    
    
    public int solution(int[][] points, int[][] routes) {
        
        for (int robot=0;robot<routes.length;robot++) {
            int cnt = 0;
            int er = 0;
            int ec = 0;
            for (int i=1;i<routes[robot].length;i++) {
                int sr = points[routes[robot][i-1]-1][0];
                int sc = points[routes[robot][i-1]-1][1];
                er = points[routes[robot][i]-1][0];
                ec = points[routes[robot][i]-1][1];
                
                cnt = move(sr,sc, er,ec, cnt);
            }
            visited[er][ec][cnt]++;
        }
        int ans = 0; 
        for (int r=0;r<101;r++) {
            for (int c=0;c<101;c++) {
                for (int cnt = 0; cnt < 20000; cnt++) {
                    if (visited[r][c][cnt] > 1) ans ++;
                }
            }
        }
        return ans;
    }
}