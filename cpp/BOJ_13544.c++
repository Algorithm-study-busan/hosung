#include <iostream>
#include <vector>
using namespace std;
#define MAX 100001

int arr[MAX] = {0,};

int upperBound(const vector<int> &arr, int x) {
    int lo = 0;
    int hi = arr.size()-1;

    while (lo <= hi) {
        int mid = (lo + hi)/2;

        if (x >= arr[mid]) lo = mid+1;
        else hi = mid-1;
    }

    return lo;
}

class MergeTree {
    public:
    vector<vector<int>> tree;

    MergeTree(int n) {
        tree.resize(n*4);
        init(1, 1, n);
    }

    void init(int node, int left, int right) {
        if (left == right) {
            tree[node] = vector<int> {arr[left]};
            return;
        }
        int mid = (left + right)/2;
        init(node*2, left, mid);
        init(node*2+1, mid+1, right);

        tree[node] = merge(tree[node*2], tree[node*2+1]);
    }

    int query(int node, int left, int right, int start, int end, int x) {
        if (right < start || left > end) return 0;
        if (start <= left && right <= end) return upperBound(tree[node], x);

        int mid = (left + right)/2;
        return query(node*2, left, mid, start, end, x) +
                query(node*2+1, mid+1, right, start, end, x);
    }

    vector<int> merge(const vector<int> &a, const vector<int> &b) {
        int ai = 0;
        int bi = 0;

        vector<int> ret;

        while(ai < a.size() && bi < b.size()) {
            if (a[ai] < b[bi]) ret.push_back(a[ai++]);
            else ret.push_back(b[bi++]);
        }

        while(ai < a.size()) {
            ret.push_back(a[ai++]);
        }

        while(bi < b.size()) {
            ret.push_back(b[bi++]);
        }

        return ret;
    }
};

int main() {
    int N; cin >> N;
    for (int i=1;i<=N;i++) cin >> arr[i];
    MergeTree megeTree = MergeTree(N);
    int M; cin >> M;

    int last = 0;
    for (int i=0;i<M;i++) {
        int a,b,c; cin >> a >> b >> c;
        a ^= last;
        b ^= last;
        c ^= last;
        last = b-a+1 - megeTree.query(1,1,N,a,b,c);
        cout << last << "\n";
    }
}