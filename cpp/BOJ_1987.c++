#include <iostream>
#include <string>
#include <vector>
using namespace std;
int R,C;
vector<string> board;
int ans = 0;
int dr[] = {-1,0,1,0};
int dc[] = {0,-1,0,1};
bool visited[26] = {0,};

bool in_range(int r, int c) {
    if (r<0 || r>=R || c<0 || c>=C) return false;
    return true;
}

void dfs(int r, int c, int cnt) {
    int x = board[r][c]-65;
    if (visited[x]) return;
    
    visited[x] = true;
    ans = max(ans, ++cnt);

    for (int i=0;i<4;i++) {
        int nr = r+dr[i];
        int nc = c+dc[i];
        if (!in_range(nr,nc)) continue;
        dfs(nr,nc,cnt);
    }
    visited[x] = false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> R >> C;
    for(int i=0;i<R;i++) {
        string s; cin >> s;
        board.push_back(s);
    }

    dfs(0,0,0);
    cout << ans;
}