package platform.work8;

public class Circle implements MyComparable{
    private int x, y, radius;

    public Circle(int x, int y, int radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    @Override
    public int compareTo(Object other) {
        if (! (other instanceof Circle)) return -2;
        Circle otherCircle = (Circle) other;
        if (radius < otherCircle.radius) return -1;
        else if (radius == otherCircle.radius) return 0;
        else return 1;
    }

    @Override
    public boolean equal(Object other) {
        if ( ! (other instanceof Circle) ) return false;
        Circle otherCircle = (Circle) other;
        return x == otherCircle.x && y == otherCircle.y && radius == otherCircle.radius;
    }

    @Override
    public String toString() {
        return String.format("Circle{x=%d, y=%d, radius=%d}", x, y, radius);
    }
}
