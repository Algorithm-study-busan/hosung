#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 2000
#define ll long long 
vector<pair<int,int>> arr;
int tree[MAX*4] = {0,};

int update(int node, int left, int right, int idx) {
    if (right < idx || idx < left) return tree[node];
    if (left == right) return ++tree[node];
    int mid = (left + right)/2;
    return tree[node] = update(node*2, left, mid, idx)
                        + update(node*2+1, mid+1, right, idx);
}

int cal(int node, int left, int right, int idx) {
    if (left >= idx) return tree[node];
    if (right < idx) return 0;
    int mid = (left+right)/2;
    return cal(node*2, left, mid, idx) +
            cal(node*2+1, mid+1, right, idx);
}

int main() {
    int V,E; cin >> V >> E;
    for (int i=0;i<E;i++) {
        int a,b; cin >> a >> b;
        arr.push_back({a,b});
    }
    sort(arr.begin(), arr.end());
    
    ll ans = 0;
    for (auto p : arr) {
        update(1,1,V,p.second);
        ans += cal(1,1,V,p.second+1);
    }
    cout << ans;
}