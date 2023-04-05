import java.io.*;
import java.util.*;
public class note {
    static int count=0;
    static int k;
    static int N;
    static boolean[][] map;
    static void countHome(int a, int b){
        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};
        k++;
        if (map[a][b]) {
            for (int i = 0; i < 4; i++) {
                if (a+dx[i]<0 || a+dx[i] >= N || b+dy[i]<0 ||b+dy[i]>=N) {
                    continue;
                }
                map[a][b] = false;
                if (map[a+dx[i]][b+dy[i]]){
                    countHome(a+dx[i], b+dy[i]);
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            String b = br.readLine();
            for (int j = 0; j < N; j++) {
                if (b.charAt(j) == '1') {
                    map[i][j] = true;
                }
                else map[i][j] = false;
            }
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(map[i][j]){
                    k = 0;
                    countHome(i,j);
                    result.add(k);
                    count++;
                }
            }
        }
        System.out.println(count);
        Collections.sort(result);
        for(int res : result) {
            System.out.println(res);
        }
    }
}