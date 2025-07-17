import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;
public class Main {
    public static void main(String args[]) throws IOException {
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] population = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0;i<N;i++) {
            population[i] = Integer.parseInt(st.nextToken());
        }
        ArrayList<Integer>[] edges = new ArrayList[N];
        for (int i=0;i<N;i++) {
            edges[i] = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            for (int j=0;j<k;j++) {
                edges[i].add(Integer.parseInt(st.nextToken())-1);
            }
        }

        // 알고리즘 - 완전탐색 + bfs
        // 시간 복잡도 : 2**N * (V+E)  [N = 10, V = 100, E~=10000]
        int total = 1 << N;

        int ans = 987654321;
        // 각 노드를 2개의 집합으로 나누는 모든 경우
        // 노드의 개수 = 비트 자리수 
        // 각 자리 별 : 1->그룹1, 0->그룹2
        for (int i=1;i<total-1;i++) {
            if (i > (i ^ (total-1))) continue; // 중복 그룹 생략
            boolean[] g1 = new boolean[N];
            boolean[] g2 = new boolean[N];
            for (int j=0;j<N;j++) {
                if ((i & (1 << j)) == (1 << j)) {
                    g1[j] = true;
                } else {
                    g2[j] = true;
                }
            }
            // 각 그룹이 연결되어 있는지 확인
            int k1 = cal(edges, g1, population);
            int k2 = cal(edges, g2, population);

            if (k1 == -1 || k2 == -1) continue; // 두 그룹이 모두 연결되어 있지 않다면 패스
            ans = Math.min(ans, Math.abs(k1-k2)); // 연결되어 있다면 차이를 최소값으로 갱신
        }
        System.out.println(ans == 987654321 ? -1 : ans);
    }

    // bfs 로 그룹 내의 노드들이 모두 연결되었는지 확인
    // 연결 x -> -1 반환 
    // 연결 0 -> 노드들의 인구 수 합 반환
    public static int cal(ArrayList<Integer>[] edges, boolean[] g, int[] population) {
        // bfs 탐색 시작 노드 찾기 
        int s = -1;
        for (int i=0;i<g.length;i++) {
            if (g[i]) {
                s=i;
                break;
            }
        }
        g[s] = false;
        int ret = population[s];

        // bfs 
        Deque<Integer> q = new LinkedList<>();
        q.add(s);
        while (!q.isEmpty()) {
            int cur = q.pollFirst();
            for (int nxt : edges[cur]) {
                if (!g[nxt]) continue;
                g[nxt] = false;
                ret += population[nxt];
                q.add(nxt);
            }
        }

        // 모두 방문하지 못했다면 -1 
        for (int i=0;i<g.length;i++) {
            if (g[i]) return -1; 
        }
        // 모두 방문했다면 인구 수 합 
        return ret;
    }
}
