#include <iostream>
using namespace std;
#define MAX 200000
#define ll long long
#define MOD 1000000007

ll valueTree[MAX*4] = {0,};
int cntTree[MAX*4] = {0,};

void valueUpdate(int node, int start, int end, int idx, int value) {
    if (idx < start || idx > end) return;
    valueTree[node] += value;
    if (start == end) return;
    int mid = (start + end) / 2;
    valueUpdate(node*2, start, mid, idx, value);
    valueUpdate(node*2+1, mid+1, end, idx, value);
}

void cntUpdate(int node, int start, int end, int idx, int value) {
    if (idx < start || idx > end) return;
    cntTree[node] += value;
    if (start == end) return;
    int mid = (start + end) / 2;
    cntUpdate(node*2, start, mid, idx, value);
    cntUpdate(node*2+1, mid+1, end, idx, value);
}

ll findValue(int node, int start, int end, int left, int right) {
    if (left <= start && end <= right) return valueTree[node];
    if (end < left || start > right) return 0;
    int mid = (start + end) / 2;
    return findValue(node*2, start, mid, left, right) 
         + findValue(node*2+1, mid+1, end, left, right);
}

int findCnt(int node, int start, int end, int left, int right) {
    if (left <= start && end <= right) return cntTree[node];
    if (end < left || start > right) return 0;
    int mid = (start + end) / 2;
    return findCnt(node*2, start, mid, left, right)
         + findCnt(node*2+1, mid+1, end, left, right);
}

int main() {
    int N; cin >> N;
    ll ans = 1;
    for (int i=0;i<N;i++) {
        int x; cin >> x;

        int leftCnt = findCnt(1, 0, MAX, 0, x);
        ll leftSum = findValue(1, 0, MAX, 0, x);
        ll leftCost = x * leftCnt - leftSum;

        int rightCnt = findCnt(1, 0, MAX, x, MAX); 
        ll rightSum = findValue(1, 0, MAX, x, MAX);
        ll rightCost = rightSum - x * rightCnt;

        
        valueUpdate(1, 0, MAX, x, x);
        cntUpdate(1, 0, MAX, x, 1);
        

        if (i == 0) continue;
        ans *= (leftCost + rightCost) % MOD;
        ans %= MOD;
        // cout << leftCnt << " " << leftSum << " " << rightCnt << " " << rightSum << endl;
        // cout << leftCost << " " << rightCost << endl;
    }
    cout << ans;
}