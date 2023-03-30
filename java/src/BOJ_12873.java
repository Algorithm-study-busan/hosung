import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_12873 {
    static int N,M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        FenwickTree fenwickTree = new FenwickTree(N);

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 1) {
                fenwickTree.update(b, c);
            }
            else {
                sb.append(fenwickTree.sum(c) - fenwickTree.sum(b - 1) + "\n");
            }
        }
        System.out.println(sb.toString());
    }

    static class FenwickTree {
        int n;
        Long[] tree;

        public FenwickTree(int n) {
            this.n = n;
            tree = new Long[n + 1];
            Arrays.fill(tree, 0L);
        }

        public void update(int idx, int val) {
            for (int i = idx; i <= n; i += (i & -i)) {
                tree[i] += val;
            }
        }

        public Long sum(int idx) {
            Long ret = 0L;
            for (int i = idx; i > 0; i -= (i & -i)) {
                ret += tree[i];
            }
            return ret;
        }
    }
}
