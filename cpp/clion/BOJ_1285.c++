#include <iostream>
#include <string>
#include <vector>
using namespace std;
bool board[20][20] = {0,};
int N;
int ans = 987654321;

int col_sum(int c) {
    int ret = 0;
    for (int r = 0; r < N; r++) {
        ret += board[r][c];
    }
    return ret;
}

int check() {
    int ret = 0;
    for (int c = 0; c < N; c++) {
        int s = col_sum(c);
        ret += min(s, N - s);
    }
    return ret;
}



void change(int k) {
    for (int i = 0; i < N; i++) {
        board[k][i] = !board[k][i];
    }
}
void dfs(int k) {
    if (k == N) {
        ans = min(ans, check());
        return;
    }

    dfs(k+1);
    change(k);
    dfs(k + 1);
    change(k + 1);
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        string s; cin >> s;
        for (int j = 0; j < N; j++) {
            board[i][j] = s[j] == 'T';
        }
    }

    dfs(0);
    cout << ans;
}