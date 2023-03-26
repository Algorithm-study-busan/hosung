import java.util.ArrayList;

public class note {
    static int R,C;

    public static int cal() {
        return 1;
    }

    static class Point {
        int x, y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static String[] f() {
        return new String[]{"asd","ASd"};
    }
    public static void main(String[] args) {
        Point point1 = new Point(1,2);
        Point point2 = new Point(1,2);
        System.out.println(point1 == point2);
    }
}
