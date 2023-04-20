#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define INF 987654321


vector<vector<bool>> board(10, vector<bool>(10, false));
int ans = INF;
int dr[] = {-1,0,1,0};
int dc[] = {0,1,0,-1};

bool inRange(int r, int c) {
    return (r >= 0 && r < 10 && c >= 0 && c < 10);
}

void buttonPush(int r, int c, vector<vector<bool>> &board) {
    board[r][c] = !board[r][c];
    for (int i=0;i<4;i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (inRange(nr, nc)) board[nr][nc] = !board[nr][nc];
    }
}

void solve(vector<vector<bool>> &board, int cnt) {

    for (int r=1;r<10;r++) {
        for (int c=0;c<10;c++) {
            if (board[r-1][c] == true) {
                buttonPush(r, c, board);
                cnt++;
            }
        }
    }

    for (int r=0;r<10;r++) {
        for (int c=0;c<10;c++) {
            if (board[r][c] == true) return;
        }
    }

    ans = min(ans, cnt);
}

void brute(int c, int cnt) {
    
    if (c == 10) {
        vector<vector<bool>> boardCopy = board;
        solve(boardCopy, cnt);
        return;
    }
    brute(c+1, cnt);
    buttonPush(0, c, board);
    brute(c+1, cnt+1);
    buttonPush(0, c, board);
}

int main() {
    for(int i=0;i<10;i++) {
        string s; cin >> s;
        for (int j=0;j<10;j++) {
            board[i][j] = (s[j] == 'O' ? true : false);
        }
    }

    brute(0,0);
    cout << (ans == INF ? -1 : ans);
}