package platform;

import java.util.Scanner;

public class StringCompareMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.nextLine();
        String s2 = scanner.nextLine();

        System.out.println(s1.equals(s2));
        System.out.println(s1.equalsIgnoreCase(s2));
        s2 = s2.toLowerCase();
        System.out.println(s1.equals(s2));
        s1 = s1.replaceAll("easy", "fun");
        System.out.println(s1.equals(s2));
    }
}
