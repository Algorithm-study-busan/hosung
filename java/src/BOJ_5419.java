import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_5419 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            ArrayList<Point> pointArr = new ArrayList<>();
            for (int n = 0; n < N; n++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                pointArr.add(new Point(x, y));
            }

            compressY(pointArr);

            Collections.sort(pointArr, new Comparator<Point>() {
                @Override
                public int compare(Point o1, Point o2) {
                    if (o1.x == o2.x) {
                        if (o1.y < o2.y) return -1;
                        return 1;
                    }
                    if (o1.x < o2.x) return -1;
                    return 1;
                }
            });

            FenwickTree fenwickTree = new FenwickTree();

            Long ans = 0L;
            for (Point point : pointArr) {
                ans += fenwickTree.get(point.y);
                fenwickTree.update(point.y);
            }
            sb.append(ans + "\n");
        }
        System.out.println(sb.toString());
    }

    static class Point {
        int x,y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static void compressY(ArrayList<Point> pointArr) {
        Collections.sort(pointArr, new Comparator<Point>() {
            @Override
            public int compare(Point o1, Point o2) {
                if (o1.y > o2.y) return -1;
                return 1;
            }
        });
        int y = 1;
        int last = pointArr.get(0).y;
        for (Point point : pointArr) {
            int curY = point.y;
            point.y = (point.y == last ? y : ++y);
            last = curY;
        }
    }

    static class FenwickTree {
        Long tree[] = new Long[75001];

        public FenwickTree() {
            Arrays.fill(tree, 0L);
        }

        public Long get(int idx) {
            Long ret = 0L;
            for (int i = idx; i > 0; i -= (i & -i)) {
                ret += tree[i];
            }
            return ret;
        }

        public void update(int idx) {
            for (int i = idx; i <= 75000; i += (i & -i)) {
                tree[i]++;
            }
        }
    }
}
