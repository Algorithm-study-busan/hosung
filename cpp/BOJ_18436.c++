#include <iostream>
using namespace std;
#define MAX 100001
int tree[MAX*4] = {0,};
int arr[MAX] = {0,};
int N;

int init(int node, int left, int right) {
    if(left == right) {
        tree[node] = (arr[left] % 2 == 0 ? 1 : 0);
        return tree[node];
    }
    int mid = (left+right)/2;
    return tree[node] = init(node*2, left, mid) + 
                init(node*2+1, mid+1, right);
}

int update(int node, int left, int right, int idx, int val) {
    if (idx < left || idx > right) return tree[node];
    if (left == right) {
        tree[node] = (val % 2 == 0 ? 1 : 0);
        return tree[node];
    }

    int mid = (left + right)/2;
    return tree[node] = update(node*2, left, mid, idx, val) +
                         update(node*2+1, mid+1, right, idx, val);
}

int query(int node, int left, int right, int start, int end) {
    if (right < start || left > end) return 0;
    if (start <= left && right <= end) return tree[node];
    int mid = (left + right)/2;
    return query(node*2, left, mid, start, end) + 
            query(node*2+1, mid+1, right, start, end);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> N;
    for(int i=1;i<=N;i++) cin >> arr[i];
    init(1, 1, N);

    int M; cin >> M;
    for (int i=0;i<M;i++) {
        int a,b,c; cin >> a >> b >> c;
        if (a == 1) {
            update(1, 1, N, b, c);
        }
        else if (a == 2) {
            cout << query(1,1,N,b,c) << "\n";
        }
        else {
            cout << c-b+1 - query(1,1,N,b,c) << "\n";
        }
    }
}

