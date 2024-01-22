#include <iostream>
#include <cstring>
using namespace std;
int dp[1000];
int arr[1000];
int N,M; 

int find_dp(int idx) {
    if (idx == N-1) return 0;
    if (dp[idx] != -1) return dp[idx];

    int a = 2;
    int ret = (M-arr[idx])*(M-arr[idx]) + find_dp(idx+1);
    int tmp = arr[idx];

    for (int i=idx+1;i<N;i++) {
        tmp += arr[i] + 1;
        if (tmp > M) break;
        if (i == N-1) {
            dp[idx] = 0;
            return 0; 
        }

        ret = min(ret, (M-tmp) * (M-tmp) + find_dp(i+1));
    }

    dp[idx] = ret;
    return ret;
}

int main() {
    memset(dp, -1, sizeof(dp));
    cin >> N >> M;
    for (int i=0;i<N;i++) cin >> arr[i];

    cout << find_dp(0);
}