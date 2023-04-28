#include <iostream>
#include <vector>
using namespace std;
#define MAX 100001

int ans[MAX] = {0,};

class SegTree {
    public:
    vector<int> tree;

    SegTree(int n) {
        tree = vector<int>(n*4, 0);
        init(1, 1, n);
    }

    int init(int node, int left, int right) { 
        if (left == right) return tree[node]=1;
        int mid = (left + right)/2;
        return tree[node] = init(node*2, left, mid) +
                            init(node*2+1, mid+1, right);
    }

    int query(int node, int left, int right, int x) {
        if (left == right) return left;
        int mid = (left + right)/2;
        if (x < tree[node*2]) return query(node*2, left, mid, x);
        else return query(node*2+1, mid+1, right, x-tree[node*2]);
    }

    int update(int node, int left, int right, int idx) {
        if (idx < left || idx > right) return tree[node];
        if (left == right) return tree[node] -= 1;
        int mid = (left + right)/2;
        return tree[node] = update(node*2, left, mid, idx) +
                            update(node*2+1, mid+1, right, idx);
    }
};

int main() {
    int N; cin >> N;
    SegTree segTree = SegTree(N);

    for (int n=1;n<=N;n++) {
        int x; cin >> x;
        int idx = segTree.query(1, 1, N, x);
        ans[idx] = n;
        segTree.update(1,1,N,idx);
    }
    for (int n=1;n<=N;n++) {
        cout << ans[n] << "\n";
    }
}