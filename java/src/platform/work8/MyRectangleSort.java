package platform.work8;

public class MyRectangleSort {
    public static void sort(MyComparable[] elements) {
        for (int i = 0; i < elements.length; i++) {
            for (int j = i + 1; j < elements.length; j++) {
                if (elements[i].compareTo(elements[j]) < 0) {
                    MyComparable temp = elements[i];
                    elements[i] = elements[j];
                    elements[j] = temp;
                }
            }
        }
    }
}
