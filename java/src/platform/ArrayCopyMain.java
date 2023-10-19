package platform;

import java.util.Arrays;
import java.util.Scanner;

public class ArrayCopyMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        int[] arrShallowCopy = arr;
        modifyArray(arrShallowCopy, 1);
        System.out.println("Shallow Copy: " + Arrays.toString(arr));

        int[] arrDeepCopy = new int[n];
        System.arraycopy(arr, 0, arrDeepCopy, 0, n);
        modifyArray(arrDeepCopy, 2);
        System.out.println("Deep Copy: " + Arrays.toString(arr));
    }

    private static void modifyArray(int[] array, int index){
        array[index] = 15;
    }
}
