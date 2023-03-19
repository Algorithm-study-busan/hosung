#include <iostream>
#include <string>
#include <vector>
using namespace std;
int R,C;
vector<string> board;
int ans = 0;
int dr[] = {-1,0,1,0};
int dc[] = {0,-1,0,1};
bool visited[20][20] = {0,};

bool in_range(int r, int c) {
    if (r<0 || r>=R || c<0 || c>=C) return false;
    return true;
}

bool contain(const vector<char> &path, char c) {
    for(char p : path) {
        if (p == c) return true;
    }
    return false;
}

void dfs(int r, int c, vector<char> &path) {
    if (visited[r][c] || contain(path, board[r][c])) return;
    
    visited[r][c] = true;
    path.push_back(board[r][c]);
    ans = max(ans, (int)path.size());

    for (int i=0;i<4;i++) {
        int nr = r+dr[i];
        int nc = c+dc[i];
        if (!in_range(nr,nc)) continue;
        dfs(nr,nc,path);
    }
    visited[r][c] = false;
    path.pop_back();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> R >> C;
    for(int i=0;i<R;i++) {
        string s; cin >> s;
        board.push_back(s);
    }

    vector<char> path;
    dfs(0,0,path);
    cout << ans;
}