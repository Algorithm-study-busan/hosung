import java.util.*;

class Solution {
    public int[] trapIdx = new int[1001];
    List<List<Edge>> edges = new ArrayList<>();
    
    public class Edge {
        int to;
        int cost;
        boolean direct;
        
        public Edge(int to, int cost, boolean direct) {
            this.to = to;
            this.cost = cost;
            this.direct = direct;
        }
    }
    
    public class Node implements Comparable<Node>{
        public int num;
        public int dist;
        public boolean[] pressed = new boolean[10];
        
        public Node(int num, int dist, boolean[] pressed) {
            this.num = num;
            this.dist = dist;
            for (int i=0;i<10;i++) {
                this.pressed[i] = pressed[i];
            }
        }
        
        @Override
        public int compareTo(Node other) {
            if (this.dist < other.dist) return -1;
            return 1;
        }
        
        public int getBit() {
            int e = 1;
            int ret = 0;
            for (int i=0;i<10;i++) {
                if (pressed[i]) ret += e;
                e *= 2;
            }
            return ret;
        }
        
        public void press() {
            if (trapIdx[num] == -1) return;
            this.pressed[trapIdx[num]] = !pressed[trapIdx[num]];
        }
        
        public boolean getDirect(int to) {
            boolean fromPressed = isPressed(num);
            boolean toPressed = isPressed(to);
            return !(fromPressed ^ toPressed);
        }
        
        public boolean isPressed(int n) {
            if (trapIdx[n] == -1) return false;
            return this.pressed[trapIdx[n]];
        }
    }
    
    public int dijkstra(int start, int end) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0, new boolean[10]));
        
        int dist[][] = new int[1001][3000];
        for (int i=0;i<1001;i++) {
            for (int j=0;j<3000;j++) {
                dist[i][j] = 987654321;
            }
        }
        
        while(!pq.isEmpty()) {
            Node cur_node = pq.poll();
            
            if (dist[cur_node.num][cur_node.getBit()] < cur_node.dist) continue;
            
            for (Edge edge : edges.get(cur_node.num)) {
                int nxt_num = edge.to;
                int nxt_dist = cur_node.dist + edge.cost;
                
                if (  (cur_node.getDirect(nxt_num) && edge.direct ) || (!cur_node.getDirect(nxt_num) && !edge.direct)  ) {
                    Node nxt_node = new Node(nxt_num, nxt_dist, cur_node.pressed);
                    nxt_node.press();
                    if (nxt_dist < dist[nxt_num][nxt_node.getBit()]) {
                        dist[nxt_num][nxt_node.getBit()] = nxt_dist;
                        pq.add(nxt_node);
                    }
                }
            }
        }
        
        int ans = 987654321;
        for (int bit=0;bit<3000;bit++) {
            ans = Math.min(ans, dist[end][bit]);
        }
        return ans;
    }
    
    
    public int solution(int n, int start, int end, int[][] roads, int[] traps) {
        for (int i=0;i<=n;i++) {
            edges.add(new ArrayList<>());
        }
        
        for (int[] road : roads) {
            edges.get(road[0]).add(new Edge(road[1], road[2], true));
            edges.get(road[1]).add(new Edge(road[0], road[2], false));
        }
        
        for (int i=0;i<1001;i++) trapIdx[i]=-1;
        for (int i=0;i<traps.length;i++) {
            trapIdx[traps[i]] = i;
        }
        
        return dijkstra(start, end);
    }
}