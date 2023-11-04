package platform.work8;

public class Circle2 implements AreaComputable{
    int x, y, radius;

    public Circle2(int x, int y, int radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    @Override
    public float getArea() {
        return radius * radius * (float)Math.PI;
    }

    @Override
    public String toString() {
        return String.format("Circle2{x=%d, y=%d, radius=%d}", x, y, radius);
    }
}
