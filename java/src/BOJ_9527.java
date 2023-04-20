import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_9527 {

    public static long cal(long n) {
        if (n == 0) return 0;

        long k = 1;
        long sumK = 1;
        long sumRet = 0;
        long sumSumRet = 0;

        while (n > sumK) {
            sumRet = k + sumSumRet;
            sumSumRet += sumRet;
            k *= 2;
            sumK += k;
        }

        return sumSumRet + (n - sumK/2) + cal(n - sumK/2 -1);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());

        System.out.println(cal(B) - cal(A - 1));
    }
}
