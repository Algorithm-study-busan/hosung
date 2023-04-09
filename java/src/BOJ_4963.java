import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_4963 {
    static int R,C;
    static int[][] board;
    static int[] dr = new int[]{-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dc = new int[]{0, 1, 1, 1, 0, -1, -1, -1};


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        while(true) {
            st = new StringTokenizer(br.readLine());
            C = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            board = new int[R][C];
            if (R == 0 && C == 0) break;
            for (int r = 0; r < R; r++) {
                st = new StringTokenizer(br.readLine());
                for (int c = 0; c < C; c++) {
                    board[r][c] = Integer.parseInt(st.nextToken());
                }
            }

            sb.append(solve() + "\n");
        }
        System.out.println(sb.toString());
    }

    static boolean inRange(int r, int c) {
        if (r < 0 || r >= R || c < 0 || c >= C) return false;
        return true;
    }

    static class Point {
        int r, c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    static int solve() {
        int ret = 0;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (board[r][c] == 0) continue;
                bfs(r, c);
                ret++;
            }
        }
        return ret;
    }

    static void bfs(int r, int c) {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(r, c));
        board[r][c] = 0;
        while (!q.isEmpty()) {
            Point cur = q.poll();

            for (int i = 0; i < 8; i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];

                if (!inRange(nr,nc) || board[nr][nc] == 0) continue;
                board[nr][nc] = 0;
                q.add(new Point(nr, nc));
            }
        }

    }
}
