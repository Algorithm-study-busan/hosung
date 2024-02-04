#include<iostream>
using namespace std;
int j,c; 

double ans = 0;

void findP(int n, int m, double p, int cnt) {
    if (cnt == c) {
        ans += p * n;
        return;
    }
    findP(n+j, m, p * n / (n+m), cnt+1);
    findP(n, m+j, p * m / (n+m), cnt+1);
}


int main() {
    int N; cin >> N;
    int n=0, m=0;
    cin >> n;
    for (int i=1;i<N;i++) {
        int x; cin >> x;
        m += x;
    }
    cin >> j >> c;

    findP(n, m, 1, 0);
    cout << ans;
}