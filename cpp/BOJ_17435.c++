#include <iostream>
using namespace std;
#define MAX 200001
int dp[20][MAX] = {0,};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int N; cin >> N; 
    for (int n=1;n<=N;n++) {
        cin >> dp[0][n];
    }

    for (int i=0;i<19;i++) {
        for (int n=1;n<=N;n++) {
            dp[i+1][n] = dp[i][dp[i][n]];
        }
    }

    int Q; cin >> Q; 
    for (int i=0;i<Q;i++) {
        int n,x; cin >> n >> x;

        for (int i=0;i<20;i++) {
            if (n % 2 == 1) {
                x = dp[i][x];
            }
            n /= 2;
        }

        cout << x << "\n";
    }
}