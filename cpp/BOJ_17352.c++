#include <iostream>
using namespace std;
#define MAX 300001

int set[MAX];
int N; 

int getParent(int a) {
    if (a == set[a]) return a;
    return set[a] = getParent(set[a]);
}

void unionNode(int a, int b) {
    a = getParent(a);
    b = getParent(b);

    if (a < b) set[b] = a;
    else set[a] = b;
}

void solve() {
    int a = getParent(1);
    for (int n=2;n<=N;n++) { 
        if (a != getParent(n)) {
            cout << a << " " << n; 
            return;
        }
    }
}

int main() {
    cin >> N;
    for (int i=1;i<=N;i++) set[i] = i;
    for (int i=0;i<N-2;i++) {
        int a,b; cin >> a >> b;
        unionNode(a,b);
    }
    solve();
}