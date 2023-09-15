package flatform;

import java.util.Scanner;
import java.util.logging.XMLFormatter;

public class AreaCalculator {
    enum x {

    }
    static final String tri = "TRIANGLE";
    static final String rec = "RECTANGLE";
    static final String cir = "CIRCLE";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean flag = true;
        while (flag) {
            String op = scanner.nextLine();
            if (op.isBlank()) continue;
            String[] opSplit = op.split(" ");
            String opToUpper = opSplit[0].toUpperCase();
            float a = 0;
            float b = 0;
            switch (opToUpper) {
                case tri:
                    a = Float.parseFloat(opSplit[1]);
                    b = Float.parseFloat(opSplit[2]);
                    System.out.printf("Area of Triangle: %.2f\n", a*b/2);
                    break;
                case rec:
                    a = Float.parseFloat(opSplit[1]);
                    b = Float.parseFloat(opSplit[2]);
                    System.out.printf("Area of Rectangle: %.2f\n", a * b);
                    break;
                case cir:
                    a = Float.parseFloat(opSplit[1]);
                    System.out.printf("Area of Circle: %.2f\n", a * a * Math.PI);
                    break;
                case "QUIT":
                    System.out.println("Bye\n");
                    flag = false;
                    break;
                default:
                    System.out.println("Invalid\n");
            }
        }
    }
}
