import javax.xml.transform.stax.StAXResult;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_9470 {
    static int inDegree[];
    static int T,t,M,P;
    static int[] cost;
    static boolean[] checked;
    static ArrayList<Integer>[] edges;

    public static int typologySort() {
        Queue<Integer> q = new LinkedList<Integer>();
        for(int n=1;n<=M;n++) {
            if (inDegree[n] == 0) {
                q.add(n);
                cost[n] = 1;
            }
        }

        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int next : edges[cur]) {
                if (cost[next] == cost[cur]) checked[next] = true;
                else if (cost[next] < cost[cur]) {
                    cost[next] = cost[cur];
                    checked[next] = false;
                }

                if (--inDegree[next] == 0) {
                    q.add(next);
                    if (checked[next]) cost[next]++;
                }
            }
        }
        return Arrays.stream(cost).max().getAsInt();
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());
        for(int i=0;i<T;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            t = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            P = Integer.parseInt(st.nextToken());
            inDegree = new int[M+1];
            edges = new ArrayList[M + 1];
            cost = new int[M + 1];
            checked = new boolean[M + 1];

            for(int j=0;j<M+1;j++) {
                edges[j] = new ArrayList<>();
            }

            for(int j=0;j<P;j++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                edges[a].add(b);
                inDegree[b] += 1;
            }
            int ans = typologySort();
            sb.append(t + " " + ans + "\n");
        }
        System.out.println(sb.toString());
    }
}
