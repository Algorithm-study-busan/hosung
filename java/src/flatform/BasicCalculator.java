package flatform;

import java.util.Objects;
import java.util.Scanner;

public class BasicCalculator {

    public static void cal(Double a, Double b, String op) {
        Double res = 0.;
        if (Objects.equals(op, "+")) {
            res = a + b;
        }
        else if (Objects.equals(op, "-")) {
            res = a - b;
        }
        else if (Objects.equals(op, "*")) {
            res = a * b;
        }
        else if (Objects.equals(op, "/")) {
            if (b == 0) {
                System.out.println("Division by zero.");
                return;
            } else {
                res = a / b;
            }
        }
        else if (Objects.equals(op, "^")) {
            res = Math.pow(a, b);
        }
        else if (Objects.equals(op, "%")) {
            res = a % b;
        }
        else {
            System.out.println("Invalid operator.");
            return;
        }
        String formatted = String.format("%.2f", res);
        System.out.println("Result: "+formatted);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < N; i++) {
            String inputLine = scanner.nextLine();
            String[] tokens = inputLine.split(" ");

            try {
                String a = tokens[0];
                String b = tokens[1];

                if (Objects.equals(b, "sqrt")) {
                    Double af = Double.parseDouble(a);
                    Double res = Math.sqrt(af);
                    String formatted = String.format("%.2f", res);
                    System.out.println("Result: " + formatted);
                } else {
                    Double af = Double.parseDouble(a);
                    Double bf = Double.parseDouble(b);
                    String op = tokens[2];
                    cal(af, bf, op);
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid number format.");
            }
        }
        scanner.close();
    }

}
