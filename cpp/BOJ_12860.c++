#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 61
#define INF 987654321
int N;
int arr[3];
int dp[MAX][MAX][MAX] = {0,};
int attack[] = {9,3,1};


void find_dp(int hp[3], int cnt) {
    if (dp[hp[0]][hp[1]][hp[2]] <= cnt) return;
    dp[hp[0]][hp[1]][hp[2]] = cnt;

    vector<int> sequence;
    for(int i=N-1;i>=0;i--) sequence.push_back(attack[i]);

    do {
        int nhp[3];
        for (int i=0;i<3;i++) nhp[i] = hp[i];
        for(int i=0;i<N;i++) {
            nhp[i] = max(nhp[i]-sequence[i], 0);
        }
        find_dp(nhp, cnt+1);
    } while(next_permutation(sequence.begin(), sequence.end()));
}

int main() {
    cin >> N;
    for(int i=0;i<MAX;i++) {
        for(int j=0;j<MAX;j++) {
            for(int k=0;k<MAX;k++) {
                dp[i][j][k] = INF;
            }
        }
    }
    int hp[3] = {0,};
    for(int i=0;i<N;i++) cin >> hp[i];

    find_dp(hp, 0);
    cout << dp[0][0][0];
}