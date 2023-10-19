package platform;

import java.util.Scanner;

public class RowColumnMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int R = scanner.nextInt();
        int C = scanner.nextInt();

        int[][] map = new int[R][C];
        int cnt = 1;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                map[r][c] = cnt++;
            }
        }

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                System.out.print(map[r][c]);
                if (c < C-1) System.out.print(", ");
            }
            System.out.print("\n");
        }
    }
}
