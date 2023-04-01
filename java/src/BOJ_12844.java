import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_12844 {
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0;i<N;i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Segtree segtree = new Segtree(N);
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int op = Integer.parseInt(st.nextToken());
            if (op == 1) {
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                int k = Integer.parseInt(st.nextToken());
                segtree.update(1, 0, N - 1, s, e, k);
            }
            else {
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                sb.append(segtree.cal(1, 0, N - 1, s, e) + "\n");
            }
        }
        System.out.println(sb.toString());
    }

    static class Segtree {
        int n;
        int[] tree;
        int[] lazy;

        public Segtree(int n) {
            this.n = n;
            tree = new int[n * 4];
            lazy = new int[n * 4];
            init(1, 0, n - 1);
        }

        public int init(int node, int left, int right) {
            if (left == right) return tree[node] = arr[left];
            int mid = (left + right) / 2;
            return tree[node] = init(node * 2, left, mid) ^ init(node * 2 + 1, mid + 1, right);
        }

        public void updateLazy(int node, int left, int right) {
            int len = (right - left + 1);
            if (lazy[node] != 0) {
                int k = lazy[node];
                if (len % 2 == 1) {
                    tree[node] ^= k;
                }
                if (left != right) {
                    lazy[node*2] ^= k;
                    lazy[node*2+1] ^= k;
                }
                lazy[node] = 0;
            }
        }

        public int update(int node, int left, int right, int start, int end, int k) {
            updateLazy(node, left, right);
            if (right < start || left > end) return tree[node];
            if (start <= left && right <= end) {
                lazy[node] ^= k;
                updateLazy(node, left, right);
                return tree[node];
            }
            int mid = (left + right) / 2;
            return tree[node] = update(node * 2, left, mid, start, end, k) ^
                    update(node * 2 + 1, mid + 1, right, start, end, k);
        }

        public int cal(int node, int left, int right, int start, int end) {
            updateLazy(node, left, right);
            if (right < start || left > end) return 0;
            if (start <= left && right <= end) return tree[node];
            int mid = (left + right) / 2;
            return cal(node * 2, left, mid, start, end) ^
                    cal(node * 2 + 1, mid + 1, right, start, end);
        }
    }
}
