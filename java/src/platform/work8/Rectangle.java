package platform.work8;

public class Rectangle implements MyComparable, AreaComputable{
    private int w, h;

    @Override
    public float getArea() {
        return w * h;
    }

    @Override
    public int compareTo(Object other) {
        if (! (other instanceof Rectangle)) return -2;
        float thisArea = getArea();
        float otherArea = ((Rectangle) other).getArea();

        if (thisArea < otherArea) return -1;
        else if (thisArea == otherArea) return 0;
        else return 1;
    }

    @Override
    public boolean equal(Object other) {
        if (! (other instanceof Rectangle)) return false;
        Rectangle otherRectangle = (Rectangle) other;
        return w == otherRectangle.w && h == otherRectangle.h;
    }

    public Rectangle(int w, int h) {
        this.w = w;
        this.h = h;
    }

    @Override
    public String toString() {
        return String.format("Rectangle{Width:    %d, Height:    %d} ", w, h);
    }
}
