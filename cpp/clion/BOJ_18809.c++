#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int R,C, gr, red;
int board[50][50] = {0,};
int dr[] = {-1, 0, 1, 0};
int dc[] = {0, -1, 0, 1};

vector< pair<int,int> > starts;

struct Node {
    int r,c;
    bool isRed;
    Node(int r, int c, bool isRed) : r(r), c(c), isRed(isRed) {}
};

bool inRange(int r, int c) {
    return r >= 0 && r < R && c >= 0 && c < C;
}

int bfs(const vector<int> &selected, vector<bool> colors) {
    bool visited[50][50] = {false,};
    queue<Node> q;

    for (int i = 0; i < starts.size(); i++) {
        if (selected[i] == 1) {
            int sr = starts[i].first;
            int sc = starts[i].second;
            bool isRed = colors.back();
            colors.pop_back();
            q.push(Node(sr, sc, isRed));
            visited[sr][sc] = true;
        }
    }

    int ret = 0;
    while (!q.empty()) {
        bool visitedRed[50][50] = {0,};
        bool visitedGreen[50][50] = {0,};
        vector<Node> can_next;
        while(!q.empty()) {
            int cr = q.front().r;
            int cc = q.front().c;
            int isRed = q.front().isRed;
            q.pop();
            for (int i = 0; i < 4; i++) {
                int nr = cr + dr[i];
                int nc = cc + dc[i];

                if (!inRange(nr,nc) ||
                    board[nr][nc] == 0 ||
                    visited[nr][nc] ) continue;
                can_next.push_back(Node(nr, nc, isRed));
                if (isRed) visitedRed[nr][nc] = true;
                else visitedGreen[nr][nc] = true;
            }
        }
        for (auto x : can_next) {
            if (visited[x.r][x.c]) continue;
            visited[x.r][x.c] = true;
            if (visitedRed[x.r][x.c] && visitedGreen[x.r][x.c]) ret += 1;
            else {
                q.push(x);
            }
        }

    }
    return ret;
}

int solve() {
    int ans = 0;
    vector<int> selected;
    vector<bool> colors;
    for(int i=0;i<gr;i++) colors.push_back(false);
    for(int i=0;i<red;i++) colors.push_back(true);

    for (int i = 0; i < starts.size(); i++) {
        if (i < starts.size() - (gr + red)) selected.push_back(0);
        else selected.push_back(1);
    }
    do {
        do {
            int x = bfs(selected, colors);
            ans = max(ans, x);
        } while (next_permutation(colors.begin(), colors.end()));
    } while (next_permutation(selected.begin(), selected.end()));
    return ans;
}

int main() {
    cin >> R >> C >> gr >> red;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            cin >> board[r][c];
            if (board[r][c] == 2) starts.push_back(make_pair(r, c));
        }
    }
    cout << solve();

}