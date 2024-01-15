#include <iostream>
#include <cstring>
using namespace std;
#define MOD 1000000007
int dp[11][100001] = {0,};
int sum[11] = {0,};
int N, K;

int main() {
    cin >> N >> K;

    for (int i=1;i<=K;i++) {
        dp[1][i] = 1;
    }
    sum[1] = K;

    for (int i=2;i<=N;i++) {
        for (int j=1;j<=K;j++) {
            int tmp = 0;
            for (int k=2*j;k<=K;k+=j) {
                tmp += dp[i-1][k];
                tmp %= MOD;
            }
            dp[i][j] = (sum[i-1] - tmp) % MOD;
            sum[i] += dp[i][j];
            sum[i] %= MOD;
        }
    }
    
    cout << sum[N];
}