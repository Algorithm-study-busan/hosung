import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10090 {
    static int N;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N + 1];

        long ans = 0;
        SegTree segTree = new SegTree(N);

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            int x = Integer.parseInt(st.nextToken());
            ans += segTree.get(1, 1, N, x);
            segTree.update(1, 1, N, x);
        }
        System.out.println(ans);
    }

    static class SegTree {
        int n;
        long[] tree;

        public SegTree(int n) {
            this.n = n;
            this.tree = new long[n * 4];
        }

        public long update(int node, int left, int right, int idx) {
            if (idx < left || right < idx) return tree[node];
            if (left == right) return tree[node] = 1;
            int mid = (left + right) / 2;
            return tree[node] = update(node * 2, left, mid, idx) +
                                update(node * 2 + 1, mid + 1, right, idx);
        }

        public long get(int node, int left, int right, int idx) {
            if (right < idx) return 0;
            if (left >= idx) return tree[node];
            int mid = (left + right)/2;
            return get(node * 2, left, mid, idx) + get(node * 2 + 1, mid + 1, right, idx);
        }
    }
}
