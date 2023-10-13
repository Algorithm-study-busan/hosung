package flatform;

public abstract class Shape {
    private int lineColor;

    public int getLineColor() {
        return lineColor;
    }

    public abstract float getLength();
    public abstract void draw();
    public abstract float getArea();

}
