package platform;

import java.util.Scanner;

public class OperatorMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        System.out.printf("%d / %d = %.3f%n", a,b, (float)a/b);
        System.out.printf("%d = %d x %d + %d", a, a/b, b, a%b);
    }
}
