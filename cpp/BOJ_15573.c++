#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MAX 1000
int board[MAX][MAX] = {0,};
int R,C,K;
int dr[] = {0,-1,0,1};
int dc[] = {-1,0,1,0};

bool in_range(int r, int c) {
    return r >= 0 and r < R and c >= 0 and c < C;
}

int count_current(bool visited[MAX][MAX], int r, int c, int k) {
    visited[r][c] = true;
    queue<pair<int,int>> q;
    q.push({r,c});

    int ret = 0;
    while(q.size()) {
        int cr = q.front().first;
        int cc = q.front().second;
        q.pop();
        ret += 1;

        for (int i=0;i<4;i++) {
            int nr = cr + dr[i];
            int nc = cc + dc[i];
            if (in_range(nr, nc) && !visited[nr][nc] && board[nr][nc] <= k) {
                visited[nr][nc] = true;
                q.push({nr, nc});
            }
        }
    }
    return ret;
}

int count_total(int k) {
    int ret = 0; 
    bool visited[MAX][MAX] = {0,};

    for (int c=0;c<C;c++) {
        if (!visited[0][c] && board[0][c] <= k) {
            ret += count_current(visited, 0, c, k);
        }
    }
    for (int r=0;r<R;r++) {
        if (!visited[r][0] && board[r][0] <= k) {
            ret += count_current(visited, r, 0, k);
        }
        if (!visited[r][C-1] && board[r][C-1] <= k) {
            ret += count_current(visited, r, C-1, k);
        }
    }
    return ret;
}

int binary_search() {
    int lo = 0;
    int hi = 1000100;

    while (lo <= hi) {
        int mid = (lo + hi)/2;

        if (count_total(mid) >= K) hi = mid-1;
        else lo = mid+1;
    }
    return lo;
}

int main() {
    cin >> R >> C >> K;
    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            cin >> board[r][c];
        }
    }
    
    cout << binary_search();
}