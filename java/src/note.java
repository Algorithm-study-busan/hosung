import java.util.ArrayList;

public class note {
    static int R,C;

    public static int cal() {
        return 1;
    }

    public static String[] f() {
        return new String[]{"asd","ASd"};
    }
    public static void main(String[] args) {
        ArrayList<Integer>[] arr = new ArrayList[5];
        for(int i=0;i<5;i++) {
            arr[i] = new ArrayList<>();
        }
        arr[0].add(5);

        System.out.println(arr[0].get(0));

    }
}
