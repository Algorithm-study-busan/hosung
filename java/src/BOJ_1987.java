import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_1987 {
    static int R,C, ans = 0;
    static Character[][] board;
    static int dr[] = {-1, 0, 1, 0};
    static int dc[] = {0, -1, 0, 1};
    static boolean[] visited = new boolean[26];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new Character[R][C];

        for (int r=0;r<R;r++) {
            String str = br.readLine();
            for (int c=0;c<C;c++) {
                board[r][c] = str.charAt(c);
            }
        }

        dfs(0, 0, 0);
        System.out.println(ans);
    }

    public static boolean inRange(int r, int c) {
        if (r<0 || r>=R || c<0 || c>=C) return false;
        return true;
    }

    public static void dfs(int r, int c, int cnt) {
        int x = board[r][c]-65;
        if (visited[x]) return;
        visited[x] = true;
        ans = Math.max(ans, ++cnt);
        for (int i=0;i<4;i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (!inRange(nr,nc)) continue;
            dfs(nr, nc, cnt);
        }
        visited[x] = false;
    }
}
