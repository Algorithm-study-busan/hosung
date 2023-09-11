#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;
vector<string> board;
int visited[5][5][5];
int dr[] = {0,-1,0,1};
int dc[] = {-1,0,1,0};
int cnt = 0;
int ans = 987654321;

bool inRange(int r, int c) {
    return r>=0 && r<5 && c>=0 && c<5;
}

void bfs(int r, int c, int k) {
    visited[k][r][c] = 0;
    queue<pair<int,int> > q;
    q.push(make_pair(r, c));
    while (!q.empty()) {
        int cr = q.front().first;
        int cc = q.front().second;
        q.pop();

        for (int i=0;i<4;i++) {
            int nr = cr + dr[i];
            int nc = cc + dc[i];
            if (!inRange(nr, nc) || visited[k][nr][nc] != -1) continue;
            visited[k][nr][nc] = visited[k][cr][cc] + 1;
            q.push(make_pair(nr, nc));
        }
    }
}

bool check(const vector<int> &arr) {
    bool star[5][5] = {0,};
    bool visited_local[5][5] = {0,};
    queue<pair<int,int> > q;
    for (int x : arr) {
        int r = x / 5;
        int c = x % 5;
        star[r][c] = true;
    }
    int sr = arr[0]/5;
    int sc = arr[0]%5;
    q.push(make_pair(sr, sc));
    visited_local[sr][sc] = true;
    int meet = 0;
    while (!q.empty()) {
        int cr = q.front().first;
        int cc = q.front().second;
        q.pop();
        meet += 1;

        for (int i=0;i<4;i++) {
            int nr = cr + dr[i];
            int nc = cc + dc[i];
            if (!inRange(nr, nc) || visited_local[nr][nc] || !star[nr][nc]) continue;
            q.push(make_pair(nr, nc));
            visited_local[nr][nc] = true;
        }
    }
    return meet == cnt;
}

void dfs(vector<int> &arr) {
    if (arr.size() == cnt) {
        if (check(arr)) {
            int tmp = 0;
            for (int k=0;k<arr.size();k++) {
                int r = arr[k] / 5;
                int c = arr[k] % 5;
                tmp += visited[k][r][c];
            }
            ans = min(ans, tmp);
        }
        return;
    }

    for (int i=0;i<25;i++) {
        arr.push_back(i);
        dfs(arr);
        arr.pop_back();
    }
}


int main() {
    for (int r=0;r<5;r++) {
        string s; cin >> s;
        board.push_back(s);
    }
    for (int i=0;i<5;i++) {
        for (int j=0;j<5;j++) {
            for (int k=0;k<5;k++) {
                visited[i][j][k] = -1;
            }
        }
    }

    for (int r=0;r<5;r++) {
        for (int c=0;c<5;c++) {
            if (board[r][c] == '*') bfs(r,c,cnt++);
        }
    }
    vector<int> arr;
    dfs(arr);
    cout << ans;
}