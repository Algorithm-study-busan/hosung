import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1259 {

    public static boolean isPalin(String x) {
        int len = x.length();
        for (int i=0;i<len/2;i++) {
            if (x.charAt(i) != x.charAt(len-i-1)) return false;
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String x = br.readLine();
            if (Integer.parseInt(x) == 0) return;
            System.out.println(isPalin(x) ? "yes" : "no");
        }
    }
}
