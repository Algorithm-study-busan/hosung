#include <vector>

using namespace std;

int MOD = 20170805;
int dp[500][500];
vector<vector<int>> board;

int find_dp(int r, int c) {
    if (r < 0 || c < 0 || board[r][c] == 1) return 0;
    if (dp[r][c] != -1) return dp[r][c];
    
    dp[r][c] = 0;
    if (board[r-1][c] == 0) {
        dp[r][c] += find_dp(r-1,c);
    }
    else if (board[r-1][c] == 2) {
        int nxt_r = r-1;
        while (nxt_r >= 0 && board[nxt_r][c] == 2) {
            nxt_r -= 1;
        }
        dp[r][c] += find_dp(nxt_r, c);
    }
    
    if (board[r][c-1] == 0) {
        dp[r][c] += find_dp(r,c-1);
    }
    else if (board[r][c-1] == 2) {
        int nxt_c = c-1;
        while (nxt_c >= 0 && board[r][nxt_c] == 2) {
            nxt_c -= 1;
        }
        dp[r][c] += find_dp(r, nxt_c);
    }
    
    dp[r][c] %= MOD;
    return dp[r][c];
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map) {
    MOD = 20170805;
    board = city_map;
    for (int i=0;i<500;i++) {
        for (int j=0;j<500;j++) {
            dp[i][j] = -1;
        }
    }
    int k = 1;
    for (int c=0;c<n;c++) {
        if (board[0][c] == 1) k=0;
        dp[0][c] = k;
    }
    k=1;
    for (int r=0;r<m;r++) {
        if (board[r][0] == 1) k=0;
        dp[r][0] = k;
    }
    
    
    
    return find_dp(m-1, n-1);
}