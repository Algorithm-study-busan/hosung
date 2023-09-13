package flatform;

import java.util.ArrayList;
import java.util.Scanner;

public class BinaryMain {
    public static void main(String[] args) {
        ArrayList<Integer> result = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int x = n;
        while (n > 0) {
            result.add(n % 2);
            n /= 2;
        }
        StringBuilder bin = new StringBuilder();
        for (int i = result.size() - 1; i >= 0; i--) {
            bin.append(result.get(i));
        }
        System.out.printf("Number %d in Binary Number: %s", x, bin);
    }
}
