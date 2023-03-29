import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_11658_2 {
    static int N,M;
    static int[][] board;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N + 1][N + 1];

        for (int r = 1; r <= N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 1; c <= N; c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        FenwickTree2D fenwickTree2D = new FenwickTree2D(N);
        for (int r = 1; r <= N; r++) {
            for (int c = 1; c <= N; c++) {
                fenwickTree2D.update(r, c, board[r][c]);
            }
        }

        for (int i=0;i<M;i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            if (w == 0) {
                int r = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());
                int diff = x - fenwickTree2D.sumRec(r, c, r, c);
                fenwickTree2D.update(r, c, diff);
            }
            else {
                int r1 = Integer.parseInt(st.nextToken());
                int c1 = Integer.parseInt(st.nextToken());
                int r2 = Integer.parseInt(st.nextToken());
                int c2 = Integer.parseInt(st.nextToken());
                sb.append(fenwickTree2D.sumRec(r1, c1, r2, c2) + "\n");
            }
        }
        System.out.println(sb.toString());
    }

    static class FenwickTree2D {
        int n;
        int tree[][];

        public FenwickTree2D(int n) {
            this.n = n;
            this.tree = new int[n + 1][n + 1];
        }

        public void update(int row, int col, int x) {
            for (int r = row; r <= N; r += (r & -r)) {
                for (int c = col; c <= N; c += (c & -c)) {
                    tree[r][c] += x;
                }
            }
        }

        public int sum(int row, int col) {
            int ret = 0;
            for (int r = row; r > 0; r -= (r & -r)) {
                for (int c = col; c > 0; c -= (c & -c)) {
                    ret += tree[r][c];
                }
            }
            return ret;
        }

        public int sumRec(int r1, int c1, int r2, int c2) {
            return sum(r2, c2) - sum(r2, c1-1) - sum(r1-1, c2) + sum(r1 - 1, c1 - 1);
        }
    }
}
