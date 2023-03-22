import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1412 {
    static int N;
    static char[][] edge;

    static boolean[][] linked;

    static void floyd() {
        for(int m=0;m<N;m++) {
            for(int s=0;s<N;s++) {
                for(int e=0;e<N;e++) {
                    if (linked[s][m] && linked[m][e]) {
                        linked[s][e] = true;
                    }
                }
            }
        }
    }

    static void solution() {
        floyd();
        for(int i=0;i<N;i++) {
            if (linked[i][i]) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        edge = new char[N][N];
        linked = new boolean[N][N];
        for(int i=0;i<N;i++) {
            String s = br.readLine();
            for (int j=0;j<N;j++) {
                edge[i][j] = s.charAt(j);
            }
        }
        for(int i=0;i<N;i++) {
            for(int j=0;j<N;j++) {
                linked[i][j] = edge[i][j] == 'Y' && edge[j][i] == 'N';
            }
        }

        solution();
    }
}
