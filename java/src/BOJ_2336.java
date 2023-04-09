import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_2336 {

    static class Node{
        int a, b, c;

        public Node(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public static Comparator<Node> NodeComparator = new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                if (o1.a < o2.a) return -1;
                return 1;
            }
        };
    }

    static class Segtree {
        int n;
        int[] tree;

        public Segtree(int n) {
            this.n = n;
            tree = new int[n * 4];
            Arrays.fill(tree, Integer.MAX_VALUE);
        }

        public int update(int node, int left, int right, int idx, int val) {
            if (idx < left || idx > right) return tree[node];
            if (left == right) return tree[node] = val;
            int mid = (left + right) / 2;
            return tree[node] = Math.min(update(node * 2, left, mid, idx, val),
                    update(node * 2 + 1, mid + 1, right, idx, val));
        }

        public int get(int node, int left, int right, int start, int end) {
            if(right < start || left > end) return Integer.MAX_VALUE;
            if(start <= left && right <= end) return tree[node];
            int mid = (left + right) / 2;
            return Math.min(get(node * 2, left, mid, start, end),
                    get(node * 2 + 1, mid + 1, right, start, end));
        }

    }

    static ArrayList<Node> arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        arr = new ArrayList<Node>();
        for (int i = 0; i < N; i++) {
            arr.add(new Node(0, 0, 0));
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            int x = Integer.parseInt(st.nextToken());
            arr.get(x-1).a = i;
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            int x = Integer.parseInt(st.nextToken());
            arr.get(x-1).b = i;
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            int x = Integer.parseInt(st.nextToken());
            arr.get(x-1).c = i;
        }
        Collections.sort(arr, Node.NodeComparator);

        Segtree segtree = new Segtree(N);
        int ans = 0;
        for (Node node : arr) {
            if (segtree.get(1, 1, N, 1, node.b) > node.c) {
                ans++;
            }
            segtree.update(1, 1, N, node.b, node.c);
        }

        System.out.println(ans);
    }
}
