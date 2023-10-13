package flatform;

public class Triangle extends Shape {
    int a;
    int b;
    int c;

    public Triangle(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    @Override
    public float getLength() {
        return a+b+c;
    }

    @Override
    public void draw() {
        System.out.printf("Triangle, Area: %.2f, Length: %.2f\n", getArea(), getLength());
    }

    @Override
    public float getArea() {
        float s = (float)(a+b+c) /2;
        return (float)Math.pow(s * (s - a) * (s - b) * (s - c), 0.5);
    }
}
