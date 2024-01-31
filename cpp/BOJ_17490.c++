#include <iostream>
#include <vector> 
#include <algorithm>
using namespace std;
#define MAX 1000001
#define ll long long
int N,M;
ll K;

vector<bool> isLink(MAX, true);
int set[MAX] = {0,};

int getParent(int n) {
    if (n == set[n]) return n;
    return set[n] = getParent(set[n]);
}

bool isSet(int a, int b) {
    a = getParent(a);
    b = getParent(b);
    return a == b;
}

void unionNode(int a, int b) {
    a = getParent(a);
    b = getParent(b);

    if (a < b) set[b] = a;
    else set[a] = b;
}

int main() {
    for (int i=0;i<MAX;i++) set[i] = i;

    cin >> N >> M >> K;
    vector<pair<int,int>> arr; 
    for (int n=1;n<=N;n++) {
        int c; cin >> c;
        arr.push_back({c, n});
    }
    sort(arr.begin(), arr.end());

    for (int i=0;i<M;i++) {
        int a, b; cin >> a >> b; 
        if (min(a,b) == 1 && max(a,b) == N) {
            isLink[N] = false;
        } else {
            isLink[min(a,b)] = false;
        }
    }

    for (int n=1;n<N;n++) {
        if (isLink[n]) unionNode(n, n+1);
    }
    if (isLink[N]) unionNode(N, 1);

    ll totalCost = 0;
    for (auto p : arr) {
        int cost = p.first;
        int node = p.second;

        if (!isSet(0, node)) {
            totalCost += cost;
            unionNode(0, node);
        }
    }
    if (M <= 1) {
        cout << "YES";
    } else {
        cout << (totalCost <= K ? "YES" : "NO");
    }
}