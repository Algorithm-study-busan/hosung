import java.util.*;

class Solution {
    public static int MAX = 1000001;
    
    public List<List<Integer>> link = new ArrayList<>();
    public boolean[] visited = new boolean[MAX];
    
    public int bfs(int start) {
        visited[start] = true;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        
        while (!q.isEmpty()) {
            int cur = q.peek();
            q.poll();
            
            if (link.get(cur).size() == 2) return 3;
            if (link.get(cur).size() == 0) return 2;
            
            
            int nxt = link.get(cur).get(0);
            if (visited[nxt]) return 1;
            q.add(nxt);
            visited[nxt] = true;
        }
        return 0;
    }
    
    public int[] solution(int[][] edges) {
        for (int i=0;i<MAX;i++) link.add(new ArrayList<>());
        
        int[] inDegree = new int[MAX];
        
        for (int i=0;i<edges.length;i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            
            inDegree[b]++;
            link.get(a).add(b);
        }
        
        int node = -1;
        for (int n=1;n<MAX;n++) {
            if (inDegree[n] == 0 && link.get(n).size() >= 2) {
                node = n;
                break;
            }
        }
        
        int[] ans = {node,0,0,0};
        
        for (int n : link.get(node)) {
            ans[bfs(n)]++;
        }
        
        return ans;
    }
}