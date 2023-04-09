import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_11405 {

    static final int S = 0;
    static final int E = 201;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        MVMF mvmf = new MVMF();

        st = new StringTokenizer(br.readLine());
        for (int n = 1; n <= N; n++) {
            int c = Integer.parseInt(st.nextToken());
            mvmf.setEdge(n, E, c, 0);
        }

        st = new StringTokenizer(br.readLine());
        for (int m = 1; m <= M; m++) {
            int c = Integer.parseInt(st.nextToken());
            mvmf.setEdge(S, m+100, c, 0);
        }

        for (int m = 101; m <= 101 + M-1; m++) {
            st = new StringTokenizer(br.readLine());
            for (int n = 1; n <= N; n++) {
                int d = Integer.parseInt(st.nextToken());
                mvmf.setEdge(m, n, Integer.MAX_VALUE, d);
            }
        }

        System.out.println(mvmf.getMinCost());
    }

    static class MVMF {

        final int MAX = 202;

        ArrayList<Integer>[] edges;

        int[][] cap;
        int[][] flow;
        int[][] dist;

        public MVMF() {
            edges = new ArrayList[MAX];
            for (int i = 0; i < MAX; i++) {
                edges[i] = new ArrayList<>();
            }
            cap = new int[MAX][MAX];
            flow = new int[MAX][MAX];
            dist = new int[MAX][MAX];
        }

        public void setEdge(int s, int e, int c, int d) {
            edges[s].add(e);
            cap[s][e] = c;
            dist[s][e] = d;

            edges[e].add(s);
            cap[e][s] = 0;
            dist[e][s] = -d;
        }

        public int getMinCost() {
            int minCost = 0;

            while (true) {
                int[] cost = new int[MAX];
                int[] path = new int[MAX];
                boolean[] inqueue = new boolean[MAX];

                Arrays.fill(cost, Integer.MAX_VALUE);
                Arrays.fill(path, -1);

                Queue<Integer> q = new LinkedList<>();
                q.add(S);
                cost[S] = 0;
                path[S] = S;
                inqueue[S] = true;

                while (!q.isEmpty()) {
                    int cur = q.poll();
                    inqueue[cur] = false;
                    for (int next : edges[cur]) {
                        int nextCost = cost[cur] + dist[cur][next];
                        if (cap[cur][next] - flow[cur][next] > 0 && cost[next] > nextCost) {
                            cost[next] = nextCost;
                            path[next] = cur;
                            if (!inqueue[next]) {
                                q.add(next);
                                inqueue[next] = true;
                            }
                        }
                    }
                }

                if (path[E] == -1) break;

                int tmp = Integer.MAX_VALUE;
                for (int i = E; i != path[i]; i = path[i]) {
                    tmp = Math.min(tmp, cap[path[i]][i] - flow[path[i]][i]);
                }

                for (int i = E; i != path[i]; i = path[i]) {
                    flow[path[i]][i] += tmp;
                    flow[i][path[i]] -= tmp;
                    minCost += dist[path[i]][i] * tmp;
                }
            }
            return minCost;
        }
    }
}
