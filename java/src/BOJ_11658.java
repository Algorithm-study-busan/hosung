import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_11658 {
    static int N,M;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        for (int r=0;r<N;r++) {
            st = new StringTokenizer(br.readLine());
            for(int c=0;c<N;c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        SegTree segTree = new SegTree();

        for (int i=0;i<M;i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            if (w == 0) {
                int r = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());
                segTree.update(1, 0, 0, N-1, N-1, r-1, c-1, x);
            }
            else {
                int r1 = Integer.parseInt(st.nextToken());
                int c1 = Integer.parseInt(st.nextToken());
                int r2 = Integer.parseInt(st.nextToken());
                int c2 = Integer.parseInt(st.nextToken());
                sb.append(segTree.sum(1, 0, 0, N-1, N - 1,
                                r1 - 1, c1 - 1, r2 - 1, c2 - 1) + "\n");
            }
        }
        System.out.println(sb.toString());
    }

    static class SegTree {
        int tree[] = new int[5000000];

        public SegTree() {
            this.init(1, 0, 0, N - 1, N - 1);
        }

        public int init(int node, int r1, int c1, int r2, int c2) {
            if (r1 == r2) {
                tree[node] = board[r1][c1];
                return tree[node];
            }
            int mr = (r1+r2)/2;
            int mc = (c1+c2)/2;
            tree[node] = init(node * 4, r1, c1, mr, mc) +
                    init(node * 4 + 1, r1, mc + 1, mr, c2) +
                    init(node * 4 + 2, mr + 1, c1, r2, mc) +
                    init(node * 4 + 3, mr + 1, mc + 1, r2, c2);
            return tree[node];
        }

        public int sum(int node, int r1, int c1, int r2, int c2,
                                 int xr1, int xc1, int xr2, int xc2) {
            if (c2 < xc1 || c1 > xc2 || r2 < xr1 || r1 > xr2) return 0;
            if (xr1 <= r1 && r2 <= xr2 && xc1 <= c1 && c2 <= xc2) {
                return tree[node];
            }
            int mr = (r1+r2)/2;
            int mc = (c1+c2)/2;
            return sum(node * 4, r1, c1, mr, mc, xr1, xc1, xr2, xc2) +
                    sum(node * 4 + 1, r1, mc + 1, mr, c2, xr1, xc1, xr2, xc2) +
                    sum(node * 4 + 2, mr + 1, c1, r2, mc, xr1, xc1, xr2, xc2) +
                    sum(node * 4 + 3, mr + 1, mc + 1, r2, c2, xr1, xc1, xr2, xc2);
        }

        public int update(int node, int r1, int c1, int r2, int c2, int xr, int xc, int val) {
            if (!(r1 <= xr && xr <= r2 && c1 <= xc && xc <= c2)) {
                return tree[node];
            }
            if(r1 == r2) {
                tree[node] = val;
                return tree[node];
            }
            int mr = (r1+r2)/2;
            int mc = (c1+c2)/2;
            tree[node] = update(node * 4, r1, c1, mr, mc, xr, xc, val) +
                    update(node * 4 + 1, r1, mc + 1, mr, c2, xr, xc, val) +
                    update(node * 4 + 2, mr + 1, c1, r2, mc, xr, xc, val) +
                    update(node * 4 + 3, mr + 1, mc + 1, r2, c2, xr, xc, val);
            return tree[node];
        }
    }
}
