#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MAX 1000
int R,C;
int board[MAX][MAX] = {0,};
int day[MAX][MAX];
int dr[] = {-1,0,1,0};
int dc[] = {0,-1,0,1};

bool inRange(int r, int c) {
    return r >= 0 && r < R && c >= 0 && c < C;
}

void bfs(queue<pair<int,int>> &q) {
    while(!q.empty()) {
        int cr = q.front().first;
        int cc = q.front().second;
        q.pop();

        for (int i=0;i<4;i++) {
            int nr = cr + dr[i];
            int nc = cc + dc[i];
            if (!inRange(nr,nc) || day[nr][nc] >= 0 || board[nr][nc] == -1) continue;
            day[nr][nc] = day[cr][cc] + 1;
            q.push({nr,nc});
        }
    }
}

void solve() {
    int ans = 0;
    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            if (board[r][c] == 0) {
                if (day[r][c] == -1) {
                    cout << -1;
                    return;
                }
                ans = max(ans, day[r][c]);
            }
        }
    }
    cout << ans;
}

int main() {
    cin >> C >> R;
    queue<pair<int,int>> q;
    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            day[r][c] = -1;
        }
    }
    
    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            cin >> board[r][c];
            if (board[r][c] == 1) {
                q.push({r,c});
                day[r][c] = 0;
            }
        }
    }
    
    bfs(q);
    solve();
}