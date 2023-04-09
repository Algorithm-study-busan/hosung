import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_13537 {

    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        arr = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        MergeTree mergeTree = new MergeTree(N);
        int M = Integer.parseInt(br.readLine());
        for (int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            sb.append(mergeTree.get(1, 1, N, i, j, k) + "\n");
        }
        System.out.println(sb.toString());
    }

    static class MergeTree {
        int n;
        ArrayList<Integer> tree[];

        public MergeTree(int n) {
            this.n = n;
            tree = new ArrayList[n * 4];
            for (int i = 0; i < n * 4; i++) {
                tree[i] = new ArrayList<>();
            }
            init(1, 1, n);
        }

        public void init(int node, int left, int right) {
            if (left == right) {
                tree[node].add(arr[left]);
                return;
            }
            int mid = (left + right) / 2;
            init(node * 2, left, mid);
            init(node * 2 + 1, mid + 1, right);
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
        }

        ArrayList<Integer> merge(ArrayList<Integer> a, ArrayList<Integer> b) {
            ArrayList<Integer> ret = new ArrayList<>();
            int ai = 0;
            int bi = 0;
            while (ai < a.size() && bi < b.size()) {
                if (a.get(ai) < b.get(bi)) {
                    ret.add(a.get(ai++));
                }
                else {
                    ret.add(b.get(bi++));
                }
            }

            while (ai < a.size()) {
                ret.add(a.get(ai++));
            }
            while (bi < b.size()) {
                ret.add(b.get(bi++));
            }
            return ret;
        }

        public int get(int node, int left, int right, int start, int end, int x) {
            if (right < start || left > end) return 0;
            if (start <= left && right <= end) {
                return tree[node].size() - upperBound(tree[node], x);
            }
            int mid = (left + right) / 2;
            return get(node * 2, left, mid, start, end, x) +
                    get(node * 2 + 1, mid + 1, right, start, end, x);
        }

        public int upperBound(ArrayList<Integer> a, int x) {
            int lo = 0;
            int hi = a.size()-1;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (a.get(mid) > x) hi = mid - 1;
                else lo = mid + 1;
            }
            return lo;
        }
    }
}
