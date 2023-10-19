package platform.work6;

public class MyArrayList<T> {
    private Object[] elementData;
    int idx = 0;

    public MyArrayList(int initialCapacity) {
        if (initialCapacity > 0) {
            elementData = new Object[initialCapacity];
        }
    }

    public void add(T data) {
        elementData[idx] = data;
        idx += 1;
    }

    public Object get(int i) {
        return elementData[i];
    }
}
