//package flatform;
//
//import java.awt.*;
//
//public class Rectangle {
//    private Point p1;
//    private Point p2;
//    public Rectangle(Point p1, Point p2) {
//        this.p1 = p1;
//        this.p2 = p2;
//    }
//
//    public Point getP1() {
//        return p1;
//    }
//
//    public Point getP2() {
//        return p2;
//    }
//
//    public Rectangle(Rectangle other) {
//        p1 = new Point(other.getP1().getX(), other.getP1().getY());
//        p2 = new Point(other.getP2().getX(), other.getP2().getY());
//    }
//
//    public void moveBy(int x, int y) {
//        p1.setX(p1.getX() + x);
//        p2.setX(p2.getX() + x);
//        p1.setY(p1.getY() + y);
//        p2.setY(p2.getY() + y);
//    }
//
//    public void moveBy(int position) {
//        p1.setX(p1.getX() + position);
//        p2.setX(p2.getX() + position);
//        p1.setY(p1.getY() + position);
//        p2.setY(p2.getY() + position);
//    }
//
//    @Override
//    public String toString() {
//        return String.format("Rectangle[(%d, %d), (%d, %d)]", p1.getX(), p1.getY(), p2.getX(), p2.getY());
//    }
//}