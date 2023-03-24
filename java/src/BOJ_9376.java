import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_9376 {

    static char[][] board;
    static int R,C;
    static final int INF = 987654321;
    static final int[] dr = {-1,0,1,0};
    static final int[] dc = {0,-1,0,1};

    public static class Node implements Comparable<Node>{
        int r,c,type,dist;
        public Node(int r, int c, int type, int dist) {
            this.r = r;
            this.c = c;
            this.type = type;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node other) {
            if (dist < other.dist) return -1;
            else if (dist > other.dist) return 1;
            return 0;
        }
    }

    public static boolean inRange(int r, int c) {
        if (r<0 || r>=R || c<0 || c>=C) return false;
        return true;
    }

    public static int dijkstra() {
        int type = 0;
        int[][][] dist = new int[R][C][3];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                for (int k = 0; k < 3; k++) {
                    dist[r][c][k] = INF;
                }
            }
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();

        for(int r=0;r<R;r++) {
            for(int c=0;c<C;c++) {
                if (board[r][c] == '$') {
                    dist[r][c][type] = 0;
                    pq.add(new Node(r, c, type, 0));
                    type++;
                }
            }
        }

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (dist[cur.r][cur.c][cur.type] < cur.dist) continue;

            for(int i=0;i<4;i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];
                if (!inRange(nr,nc) || board[nr][nc] == '*') continue;
                int nDist = cur.dist + (board[nr][nc] == '#' ? 1 : 0);

                if (dist[nr][nc][cur.type] > nDist) {
                    pq.add(new Node(nr, nc, cur.type, nDist));
                    dist[nr][nc][cur.type] = nDist;
                }

                if (cur.type < 2 && dist[nr][nc][(cur.type+1)%2] != INF) {
                    nDist = dist[nr][nc][(cur.type+1)%2] + cur.dist;
                    if (dist[nr][nc][2] <= nDist) continue;
                    dist[nr][nc][2] = nDist;
                    pq.add(new Node(nr, nc, 2, nDist));
                }
            }
        }

        int min0 = INF, min1 = INF, min2 = INF;
        for(int r=0;r<R;r++) {
            min0 = Math.min(min0, dist[r][0][0]);
            min1 = Math.min(min1, dist[r][0][1]);
            min2 = Math.min(min2, dist[r][0][2]);
            min0 = Math.min(min0, dist[r][C-1][0]);
            min1 = Math.min(min1, dist[r][C-1][1]);
            min2 = Math.min(min2, dist[r][C-1][2]);
        }
        for (int c=0;c<C;c++) {
            min0 = Math.min(min0, dist[0][c][0]);
            min1 = Math.min(min1, dist[0][c][1]);
            min2 = Math.min(min2, dist[0][c][2]);
            min0 = Math.min(min0, dist[R-1][c][0]);
            min1 = Math.min(min1, dist[R-1][c][1]);
            min2 = Math.min(min2, dist[R-1][c][2]);
        }
        return Math.min(min0 + min1, min2);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int i=0;i<T;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            board = new char[R][C];
            for(int r = 0; r < R; r++) {
                String s = br.readLine();
                for (int c = 0; c < C; c++) {
                    board[r][c] = s.charAt(c);
                }
            }
            sb.append(dijkstra() + "\n");
        }

        System.out.println(sb.toString());
    }
}
