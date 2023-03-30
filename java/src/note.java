import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class note {
    static LinkedList<Integer>[] edges;
    static boolean visited[];


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        edges = new LinkedList[N + 1];
        visited = new boolean[N + 1];
        for (int i = 0; i <= N; i++) {
            edges[i] = new LinkedList<Integer>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            edges[a].add(b);
            edges[b].add(a);
        }
        for (int i = 0; i <= N; i++) {
            Collections.sort(edges[i]);
        }
        dfs(S);
        visited = new boolean[N + 1];
        System.out.println();
        bfs(S);

        int[] dr = new int[]{-1, 0, 1, 0};
        int[] dc = new int[]{0, -1, 0, 1};




    }

    static void dfs(int cur) {
        visited[cur] = true;
        System.out.print(cur + " ");
        for (int next : edges[cur]) {
            if (visited[next]) continue;
            dfs(next);
        }
    }


    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            int cur = q.poll();
            System.out.print(cur + " ");
            for (int next : edges[cur]) {
                if (visited[next]) continue;
                visited[next] = true;
                q.add(next);
            }
        }
    }

}
