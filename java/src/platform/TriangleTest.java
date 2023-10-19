package platform;

import java.util.Scanner;

public class TriangleTest {
    public static class Triangle {
        private int base;
        private int height;

        public Triangle(int base, int height) {
            this.base = base;
            this.height = height;
        }

        public Double getArea() {
            return (double)base * height / 2;
        }

        @Override
        public String toString() {
            return String.format("Triangle [base=%d, height=%d, area=%.2f]", base, height, getArea());
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        for (int i = 0; i < N; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            Triangle triangle = new Triangle(a,b);
            System.out.println(triangle.toString());
        }
    }
}
