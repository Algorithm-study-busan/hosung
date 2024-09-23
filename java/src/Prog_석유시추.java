import java.util.*;

class Solution {
    public static class Point {
        public int r;
        public int c;
        
        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    
    public int[] dr = {-1,0,1,0};
    public int[] dc = {0,-1,0,1};
    public int R = 0;
    public int C = 0;
    
    public boolean visited[][] = new boolean[500][500];
    public boolean visited_oil[][] = new boolean[500][500];
    
    public int getCnt(int r, int c, int[][] land) {
        visited[r][c] = true;
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(r,c));
        
        int ret = 0;
        
        while (!q.isEmpty()) {
            Point cur = q.poll();
            ret++;
            
            for (int i=0;i<4;i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];
                
                if (nr>=0 && nr<R && nc>=0 && nc<C && land[nr][nc] == 1 && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.add(new Point(nr,nc));
                }
            }
        }
        
        return ret;
    }
    
    public void bfs(int r, int c, int[][] land, int[] oil, int cnt) {
        boolean[] visited_c = new boolean[500];
        
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(r,c));
        visited_oil[r][c] = true;
        
        while(!q.isEmpty()) {
            Point cur = q.poll();
            
            if (!visited_c[cur.c]) {
                visited_c[cur.c] = true;
                oil[cur.c] += cnt;
            }
            
            for (int i=0;i<4;i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];
                
                if (nr>=0 && nr<R && nc>=0 && nc<C && !visited_oil[nr][nc] && land[nr][nc] == 1) {
                    visited_oil[nr][nc] = true;
                    q.add(new Point(nr,nc));
                }
            }
        }
    }
    
    public int solution(int[][] land) {
        R = land.length;
        C = land[0].length;
        
        int[] oil = new int[500];
        for (int r=0;r<R;r++) {
            for (int c=0;c<C;c++) {
                if (land[r][c] == 1 && !visited[r][c]) {
                    int cnt = getCnt(r,c, land);
                    bfs(r,c, land, oil, cnt);
                }
            }
        }
        
        int ans = 0;
        for (int i=0;i<C;i++) {
            ans = Math.max(ans, oil[i]);
        }
        return ans;
    }
}