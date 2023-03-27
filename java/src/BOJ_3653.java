import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_3653 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for(int i=0;i<T;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int index[] = new int[n + 1];
            for(int j=1;j<=n;j++) {
                index[j] = j + m - 1;
            }

            SegTree segTree = new SegTree(n, m);

            st = new StringTokenizer(br.readLine());

            for(int j=m-1;j>=0;j--) {
                int x = Integer.parseInt(st.nextToken());
                int idx = index[x];

                sb.append(segTree.sum(1, 0, idx - 1, 0, n + m - 1) + " ");
                segTree.update(1, 0, n + m - 1, idx, -1);
                segTree.update(1, 0, n + m - 1, j, 1);
                index[x] = j;
            }
            sb.append("\n");
        }

        System.out.println(sb.toString());
    }

    public static class SegTree {
        int n, m;
        int tree[];

        public SegTree(int n, int m) {
            this.n = n;
            this.m = m;
            this.tree = new int[(n + m) * 4];
            this.init(1, 0, n + m - 1);
        }

        public int init(int idx, int left, int right) {
            if (left == right) {
                tree[idx] = (left < m ? 0 : 1);
                return tree[idx];
            }
            int mid = (left+right)/2;
            tree[idx] = init(idx*2, left, mid) + init(idx*2+1, mid+1, right);
            return tree[idx];
        }

        public int sum(int idx, int start, int end, int left, int right) {
            if(right < start || left > end) return 0;
            if(left >= start && right <= end) return tree[idx];
            int mid = (left+right)/2;

            return sum(idx * 2, start, end, left, mid) + sum(idx * 2 + 1, start, end, mid + 1, right);
        }

        public int update(int idx, int left, int right, int updateIdx, int updateValue) {
            if (updateIdx < left || updateIdx > right) return tree[idx];
            if (left == right) {
                tree[idx] += updateValue;
                return tree[idx];
            }
            int mid = (left + right) / 2;
            tree[idx] = update(idx * 2, left, mid, updateIdx, updateValue) +
                    update(idx * 2 + 1, mid+1, right, updateIdx, updateValue);
            return tree[idx];
        }
    }
}
