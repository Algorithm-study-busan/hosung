import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14438 {
    static int N, M;
    static int[] arr;

    static final int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(br.readLine());
        arr = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=1;i<=N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        SegTree segTree = new SegTree(N);

        M = Integer.parseInt(br.readLine());
        for(int i=0;i<M;i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 1) {
                segTree.update(1, 1, N, b, c);
            }
            else {
                sb.append(segTree.min(1, 1, N, b, c) + "\n");
            }
        }

        System.out.println(sb.toString());
    }

    static class SegTree {
        int n;
        int[] tree;

        public SegTree(int n) {
            this.n = n;
            this.tree = new int[n * 4];
            this.init(1, 1, n);
        }

        public int init(int idx, int left, int right) {
            if (left == right) {
                tree[idx] = arr[left];
                return tree[idx];
            }
            int mid = (left + right) / 2;
            tree[idx] = Math.min(init(idx * 2, left, mid), init(idx * 2 + 1, mid + 1, right));
            return tree[idx];
        }

        public int min(int idx, int left, int right, int start, int end) {
            if (end < left || start > right) return 987654321;
            if (start <= left && right <= end) return tree[idx];
            int mid = (left + right) / 2;
            return Math.min(min(idx * 2, left, mid, start, end),
                    min(idx * 2 + 1, mid + 1, right, start, end));
        }

        public int update(int idx, int left, int right, int updateIdx, int updateVal) {
            if (updateIdx < left || updateIdx > right) return tree[idx];
            if (left == right) {
                tree[idx] = updateVal;
                return tree[idx];
            }
            int mid = (left+right)/2;
            tree[idx] = Math.min(update(idx * 2, left, mid, updateIdx, updateVal),
                    update(idx * 2 + 1, mid + 1, right, updateIdx, updateVal));
            return tree[idx];
        }
    }
}
