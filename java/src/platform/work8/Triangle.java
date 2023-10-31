package platform.work8;

public class Triangle implements AreaComputable{
    int x,y;

    public Triangle(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public float getArea() {
        return (float) x * y / 2;
    }

    @Override
    public String toString() {
        return String.format("Triangle{Width:    %d, Height:    %d} ", x, y);
    }
}
