#include <iostream>
#include <queue> 
using namespace std;
int before[30][30] = {0,};
int after[30][30] = {0,};
int R,C;
int dr[] = {-1,0,1,0};
int dc[] = {0,-1,0,1};

bool visited[30][30] = {0,};

bool inRange(int r, int c) {
    return r >= 0 && r < R && c >= 0 && c < C;
}

void bfs(int sr, int sc, int beforeNum, int afterNum) {
    visited[sr][sc] = true;
    queue<pair<int,int>> q;
    q.push({sr, sc});
    before[sr][sc] = afterNum;

    while(!q.empty()) {
        int cr = q.front().first;
        int cc = q.front().second;
        q.pop(); 

        for (int i=0;i<4;i++) {
            int nr = cr + dr[i];
            int nc = cc + dc[i];

            if (!inRange(nr, nc) || visited[nr][nc] || before[nr][nc] != beforeNum) continue;

            q.push({nr,nc});
            visited[nr][nc] = true;
            before[nr][nc] = afterNum;
        }
    }
}

void solve() {
    int sr = -1;
    int sc = -1;

    int beforeNum = -1;
    int afterNum = -1;
    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            if (before[r][c] != after[r][c]) {
                sr = r;
                sc = c;
                beforeNum = before[r][c];
                afterNum = after[r][c];
            }
        }
    }

    if (sr == -1 && sc == -1) {
        cout << "YES";
        return;
    }

    bfs(sr, sc, beforeNum, afterNum);

    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            if (before[r][c] != after[r][c]) {
                cout << "NO";
                return;
            }
        }
    }
    cout << "YES";
}

int main() {
    cin >> R >> C;
    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            cin >> before[r][c];
        }
    }

    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            cin >> after[r][c];
        }
    }

    solve();
}