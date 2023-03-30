import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_7469 {
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        arr = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for(int i=1;i<=N;i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Segtree segtree = new Segtree(N);
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            sb.append(segtree.binarySearch(a, b, c) + "\n");
        }

        System.out.println(sb.toString());
    }

    static class Segtree {
        int n;
        ArrayList<Integer>[] tree;

        public Segtree(int n) {
            this.n = n;
            tree = new ArrayList[n*4];
            for (int i = 0; i < n*4; i++) {
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

        public ArrayList<Integer> merge(ArrayList<Integer> a, ArrayList<Integer> b) {
            ArrayList<Integer> ret = new ArrayList<>();

            int ai = 0, bi = 0;
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
                return upperBound(tree[node], x);
            }
            int mid = (left + right) / 2;
            return get(node * 2, left, mid, start, end, x) +
                    get(node*2+1, mid+1, right, start, end, x);
        }

        public int binarySearch(int start, int end, int idx) {
            int lo = (int) -1e9;
            int hi = (int) 1e9;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                int midIdx = get(1, 1, n, start, end, mid);
                if (idx <= midIdx) hi = mid-1;
                else lo = mid+1;
            }
            return lo;
        }

        public static int upperBound(List<Integer> arr, int x) {
            int lo = 0;
            int hi = arr.size()-1;

            while (lo <= hi) {
                int mid = (lo + hi)/2;
                if (x >= arr.get(mid)) lo = mid+1;
                else hi = mid-1;
            }
            return lo;

        }
    }
}
