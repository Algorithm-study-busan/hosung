import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_3176 {

    static class Edge {
        int node, dist;
        public Edge(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }
    }

    static class Ans {
        int min, max;

        public Ans(int min, int max) {
            this.min = min;
            this.max = max;
        }
    }

    static int N,M, MAX_HEIGHT = 20;
    static int depth[];
    static int parent[][];
    static int minDist[][];
    static int maxDist[][];

    static ArrayList<Edge>[] edges;

    static void dfs(int par, int cur, int dep) {
        parent[cur][0] = par;
        depth[cur] = dep;

        for (Edge edge : edges[cur]) {
            if (edge.node == par) continue;
            minDist[edge.node][0] = edge.dist;
            maxDist[edge.node][0] = edge.dist;
            dfs(cur, edge.node, dep + 1);
        }
    }

    static void connection() {
        for(int k=1;k<MAX_HEIGHT;k++) {
            for(int n=1;n<=N;n++) {
                parent[n][k] = parent[parent[n][k - 1]][k - 1];
                minDist[n][k] = Math.min(minDist[parent[n][k - 1]][k - 1], minDist[n][k - 1]);
                maxDist[n][k] = Math.max(maxDist[parent[n][k - 1]][k - 1], maxDist[n][k - 1]);
            }
        }
    }

    static Ans LCA(int a, int b) {
        Ans ret = new Ans(987654321,0);
        if (depth[a] < depth[b]) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        if (depth[a] != depth[b]) {
            int diff = depth[a] - depth[b];
            for(int i=0;diff>0;i++) {
                if (diff % 2 == 1) {
                    ret.min = Math.min(ret.min, minDist[a][i]);
                    ret.max = Math.max(ret.max, maxDist[a][i]);
                    a = parent[a][i];
                }
                diff /= 2;
            }
        }

        if (a != b) {
            for(int k=MAX_HEIGHT-1;k>=0;k--) {
                if (parent[a][k] != parent[b][k]) {
                    ret.min = Math.min(ret.min, minDist[a][k]);
                    ret.max = Math.max(ret.max, maxDist[a][k]);
                    ret.min = Math.min(ret.min, minDist[b][k]);
                    ret.max = Math.max(ret.max, maxDist[b][k]);
                    a = parent[a][k];
                    b = parent[b][k];
                }
            }
            ret.min = Math.min(ret.min, minDist[a][0]);
            ret.max = Math.max(ret.max, maxDist[a][0]);
            ret.min = Math.min(ret.min, minDist[b][0]);
            ret.max = Math.max(ret.max, maxDist[b][0]);
        }
        return ret;
    }




    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(br.readLine());
        depth = new int[N + 1];
        parent = new int[N + 1][MAX_HEIGHT];
        minDist = new int[N + 1][MAX_HEIGHT];
        maxDist = new int[N + 1][MAX_HEIGHT];
        edges = new ArrayList[N + 1];

        for (int i=0;i<=N;i++) {
            edges[i] = new ArrayList<Edge>();
        }

        for (int i=0;i<N-1;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            edges[a].add(new Edge(b, c));
            edges[b].add(new Edge(a, c));
        }

        dfs(0, 1, 0);
        connection();

        M = Integer.parseInt(br.readLine());
        for (int i=0;i<M;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            Ans ans = LCA(a, b);
            sb.append(ans.min + " " + ans.max + "\n");
        }

        System.out.println(sb.toString());
    }
}
