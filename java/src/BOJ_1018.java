import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1018 {
    static Character[][] board;
    static int R,C;

    static int cal(int r, int c) {
        char[] x = new char[]{'W', 'B'};

        int ret1 = 0;
        int ret2 = 0;

        for (int i=0;i<8;i++) {
            for (int j=0;j<8;j++) {
                int nr = r+i;
                int nc = c+j;
                ret1 += board[nr][nc] == x[(nr+nc)%2] ? 0 : 1;
                ret2 += board[nr][nc] == x[(nr+nc+1)%2] ? 0 : 1;
            }
        }
        return Math.min(ret1, ret2);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new Character[R][C];

        for (int r=0;r<R;r++) {
            String s = br.readLine();
            for (int c=0;c<C;c++) {
                board[r][c] = s.charAt(c);
            }
        }

        int ans = 987654321;
        for (int r=0;r<R-7;r++) {
            for(int c=0;c<C-7;c++) {
                ans = Math.min(ans, cal(r, c));
            }
        }
        System.out.println(ans);
    }
}
