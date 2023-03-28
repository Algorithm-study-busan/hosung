import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_16975 {
    static int N,M;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        arr = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        LazySegTree lazySegTree = new LazySegTree(N);

        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int op = Integer.parseInt(st.nextToken());

            if (op == 1) {
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                lazySegTree.update(1, 1, N, s, e, v);
            }

            else {
                int idx = Integer.parseInt(st.nextToken());
                sb.append(lazySegTree.getX(1, 1, N, idx, 0L) + "\n");
            }
        }
        System.out.println(sb.toString());
    }

    static class LazySegTree {
        int n;
        Long[] tree;

        public LazySegTree(int n) {
            this.n = n;
            this.tree = new Long[n * 4];
            Arrays.fill(tree, 0L);
            this.init(1, 1, n);
        }

        public void init(int node, int left, int right) {
            if (left == right) {
                tree[node] = Long.valueOf(arr[left]);
                return;
            }
            int mid = (left + right) / 2;
            init(node*2, left, mid);
            init(node * 2 + 1, mid + 1, right);
        }

        public void update(int node, int left, int right, int start, int end, int val) {
            if (right < start || left > end) return;
            if (start <= left && right <= end) {
                tree[node] += val;
                return;
            }
            int mid = (left + right) / 2;
            update(node * 2, left, mid, start, end, val);
            update(node * 2 + 1, mid + 1, right, start, end, val);
        }

        public Long getX(int node, int left, int right, int idx, Long ret) {
            if (idx < left || idx > right) return 0L;
            ret += tree[node];
            if (left == right) return ret;
            int mid = (left + right)/2;
            return getX(node * 2, left, mid, idx, ret) +
                    getX(node * 2 + 1, mid + 1, right, idx, ret);
        }
    }
}
