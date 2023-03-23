import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Vector;

public class BOJ_11438 {
    static int MAX_HEIGHT = 20, N, M;
    static Vector<Vector<Integer>> edges;
    static int[] depth;
    static int[][] parent;

    static void dfs(int par, int cur, int dep) {
        depth[cur] = dep;
        parent[cur][0] = par;

        for (int next : edges.get(cur)) {
            if (next == par) continue;
            dfs(cur, next, dep + 1);
        }
    }

    static void connection() {
        for(int k=1;k<MAX_HEIGHT;k++) {
            for(int n=1;n<=N;n++) {
                parent[n][k] = parent[parent[n][k - 1]][k - 1];
            }
        }
    }

    static int LCA(int a, int b) {
        if (depth[a] < depth[b]) b = swap(a, a = b);
        if (depth[a] != depth[b]) {
            int diff = depth[a] - depth[b];
            for(int i=0;diff>0;i++) {
                if(diff%2 == 1) a = parent[a][i];
                diff /= 2;
            }
        }
        if (a != b) {
            for(int k=MAX_HEIGHT-1;k>=0;k--) {
                if (parent[a][k] != parent[b][k]) {
                    a = parent[a][k];
                    b = parent[b][k];
                }
            }
            a = parent[a][0];
        }
        return a;
    }

    static int swap(int a, int b) {
        return a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(br.readLine());
        edges = new Vector<Vector<Integer>>(N + 1);
        for (int i = 0; i <= N; i++) {
            edges.add(new Vector<Integer>());
        }
        depth = new int[N + 1];
        parent = new int[N + 1][MAX_HEIGHT];

        for (int i=0;i<N-1;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            edges.get(a).add(b);
            edges.get(b).add(a);
        }

        dfs(0,1,0);
        connection();

        M = Integer.parseInt(br.readLine());
        for(int i=0;i<M;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sb.append(LCA(a, b) + "\n");
        }

        System.out.println(sb.toString());
    }
}
