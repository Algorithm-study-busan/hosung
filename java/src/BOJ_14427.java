import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14427 {

    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[N + 1];
        arr[0] = Integer.MAX_VALUE;
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        SegTree segTree = new SegTree(N);
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int op = Integer.parseInt(st.nextToken());
            if (op == 2) {
                sb.append(segTree.cal(1, 1, N, 1, N) + "\n");
            }
            else {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                arr[a] = b;
                segTree.update(1, 1, N, a);
            }
        }
        System.out.println(sb.toString());

    }

    static class SegTree {
        int n;
        int[] tree;
        public SegTree(int n) {
            this.n = n;
            tree = new int[n * 4];
            init(1, 1, n);
        }

        public int init(int node, int left, int right) {
            if (left == right) {
                tree[node] = left;
                return left;
            }
            int mid = (left + right) / 2;
            int left_idx = init(node * 2, left, mid);
            int right_idx = init(node * 2 + 1, mid + 1, right);
            if (arr[left_idx] <= arr[right_idx]) {
                tree[node] = left_idx;
            }
            else {
                tree[node] = right_idx;
            }
            return tree[node];
        }

        public int update(int node, int left, int right, int idx) {
            if (idx < left || idx > right) return tree[node];
            if (left == right) return tree[node];

            int mid = (left + right) / 2;
            int left_idx = update(node * 2, left, mid, idx);
            int right_idx = update(node * 2 + 1, mid + 1, right, idx);
            if (arr[left_idx] <= arr[right_idx]) {
                tree[node] = left_idx;
            }
            else {
                tree[node] = right_idx;
            }
            return tree[node];
        }

        public int cal(int node, int left, int right, int start, int end) {
            if (right < start || left > end) {
                return 0;
            }
            if (start <= left && end <= right) return tree[node];
            int mid = (left + right) / 2;
            int left_idx = cal(node * 2, left, mid, start, end);
            int right_idx = cal(node * 2 + 1, mid + 1, right, start, end);
            if (arr[left_idx] <= arr[right_idx]) return left_idx;
            else return right_idx;
        }
    }

}
