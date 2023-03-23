import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_14567 {
    static int N,M;
    static int[] inDegree;
    static int[] ans;
    static ArrayList<Integer>[] edges;

    static void typologySort() {
        Queue<Integer> q = new LinkedList<>();
        for(int n=1;n<=N;n++) {
            if (inDegree[n] == 0) {
                q.add(n);
                ans[n] = 1;
            }
        }

        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int next : edges[cur]) {
                if (--inDegree[next] == 0) {
                    q.add(next);
                    ans[next] = ans[cur]+1;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        inDegree = new int[N+1];
        edges = new ArrayList[N+1];
        ans = new int[N + 1];

        for(int i=0;i<N+1;i++) {
            edges[i] = new ArrayList<Integer>();
        }

        for(int i=0;i<M;i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            edges[a].add(b);
            inDegree[b] += 1;
        }

        typologySort();

        for(int n=1;n<=N;n++) {
            sb.append(ans[n] + " ");
        }

        System.out.println(sb.toString());
    }
}
