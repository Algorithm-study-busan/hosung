import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BOJ_2517 {

    static class Node {
        int idx, score;

        public Node(int idx, int score) {
            this.idx = idx;
            this.score = score;
        }

        public void setScore(int score) {
            this.score = score;
        }
    }

    static int N;

    static int[] tree;

    static void putTree(int idx, int left, int right, int val) {
        if (val < left || val > right) return;
        tree[idx]++;
        if (left == right) return;
        int mid = (left+right)/2;
        putTree(idx * 2, left, mid, val);
        putTree(idx * 2 + 1, mid + 1, right, val);
    }

    static int sumTree(int idx, int left, int right, int val) {
        if (left == right) return 0;
        int mid = (left + right) / 2;
        if (mid < val) {
            return tree[idx * 2] + sumTree(idx * 2 + 1, mid + 1, right, val);
        }
        else {
            return sumTree(idx * 2, left, mid, val);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        tree = new int[N * 4];
        Node[] arr = new Node[N];

        for(int i=0;i<N;i++) {
            int a = Integer.parseInt(br.readLine());
            arr[i] = new Node(i, a);
        }

        Arrays.sort(arr, new Comparator<Node>() {
            public int compare(Node a, Node b) {
                if (a.score < b.score) return -1;
                return 1;
            }
        });

        int newScore = 1;
        for (Node node : arr) {
            node.setScore(newScore++);
        }

        Arrays.sort(arr, new Comparator<Node>() {
            @Override
            public int compare(Node a, Node b) {
                if (a.idx < b.idx) return -1;
                return 1;
            }
        });

        for (Node node : arr) {
            sb.append(1 + node.idx - sumTree(1, 1, N, node.score) + "\n");
            putTree(1, 1, N, node.score);
        }

        System.out.println(sb.toString());
    }
}
