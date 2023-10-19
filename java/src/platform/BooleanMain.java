package platform;

import java.util.Scanner;

public class BooleanMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        System.out.println("Number1 : "+a+", Number2 : "+b);
        System.out.println("Number1 > Number2 ? " + (a > b));
        System.out.println("Number1 < Number2 ? " + (a < b));
        System.out.println("Number1 == Number2 ? " + (a == b));
    }
}
