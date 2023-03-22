import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1920 {
    public static int[] arr;

    public static boolean binarySearch(int x) {
        int lo = 0;
        int hi = arr.length-1;
        while (lo < hi) {
            int mid = (lo+hi)/2;
            if (arr[mid] < x) {
                lo = mid+1;
            }
            else hi = mid;
        }
        return arr[lo] == x;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for(int i=0;i<M;i++) {
            int x = Integer.parseInt(st.nextToken());
            System.out.println(binarySearch(x) ? 1 : 0);
        }
    }
}
