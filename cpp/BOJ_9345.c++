#include <iostream>
#include <vector>
using namespace std;
#define MAX 100000
#define INF 987654321
int arr[MAX] = {0,};

class SegTreeMin {
    public :
    vector<int> tree;

    SegTreeMin(int n) {
        tree.resize(n*4);
        init(1, 0, n-1);
    }

    int init(int node, int left, int right) {
        if (left == right) return tree[node] = arr[left];
        int mid = (left + right)/2;

        return tree[node] = min(init(node*2, left, mid),
                                init(node*2+1, mid+1, right));
    }

    int update(int node, int left, int right, int idx, int val) {
        if (idx < left || idx > right) return tree[node];
        if (left == right) return tree[node] = val;
        int mid = (left + right)/2;
        return tree[node] = min(update(node*2, left, mid, idx, val),
                                update(node*2+1, mid+1, right, idx, val));
    }

    int query(int node, int left, int right, int start, int end) {
        if (right < start || left > end) {
            return INF;
        }
        if (start <= left && right <= end) return tree[node];
        int mid = (left + right)/2;
        return min(query(node*2, left, mid, start, end),
                    query(node*2+1, mid+1, right, start, end));
    }
};

class SegTreeMax {
    public:
    vector<int> tree;
    SegTreeMax(int n) {
        tree.resize(n*4);
        init(1, 0, n-1);
    }

    int init(int node, int left, int right) {
        if (left == right) return tree[node] = arr[left];
        int mid = (left + right)/2;
        return tree[node] = max(init(node*2, left, mid),
                                init(node*2+1, mid+1, right));
    }

    int update(int node, int left, int right, int idx, int val) {
        if (idx < left || idx > right) return tree[node];
        if (left == right) return tree[node] = val;
        int mid = (left + right)/2;
        return tree[node] = max(update(node*2, left, mid, idx, val),
                                update(node*2+1, mid+1, right, idx, val));
    }

    int query(int node, int left, int right, int start, int end) {
        if (right < start || left > end) return 0;
        if (start <= left && right <= end) return tree[node];
        int mid = (left + right)/2;
        return max(query(node*2, left, mid, start, end),
                    query(node*2+1, mid+1, right, start, end));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int T; cin >> T;
    while(T--) {
        int N, M; cin >> N >> M;
        for(int i=0;i<N;i++) arr[i] = i;
        SegTreeMin segTreeMin = SegTreeMin(N);
        SegTreeMax segTreeMax = SegTreeMax(N);

        for(int i=0;i<M;i++) {
            int op, a,b; cin >> op >> a >> b;

            if (op == 0) {
                int tmp = arr[a];
                arr[a] = arr[b];
                arr[b] = tmp;

                segTreeMin.update(1, 0, N-1, a, arr[a]);
                segTreeMin.update(1, 0, N-1, b, arr[b]);

                segTreeMax.update(1, 0, N-1, a, arr[a]);
                segTreeMax.update(1, 0, N-1, b, arr[b]);
            }
            else {
                int lo = segTreeMin.query(1, 0, N-1, a, b);
                int hi = segTreeMax.query(1, 0, N-1, a, b);
                int ck = (lo == a) && (hi == b);
                cout << (ck ? "YES" : "NO") << "\n";
            }
        }
    }
} 