#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
using namespace std;
int N;
vector<string> board;
int dr[] = {-1, -1, 0, 1, 1, 0};
int dc[] = {0,1,1,0,-1,-1};
int ans = 0;
int visited[50][50];

struct Node {
    int r,c, pr, pc;
    Node(int r, int c, int pr, int pc) : r(r), c(c), pr(pr), pc(pc) {}
};

bool inRange(int r, int c) {
    return r>=0 && r<N && c>=0 && c<N;
}

void bfs(int r, int c) {
    queue<Node> q;
    q.push(Node(r, c, -1, -1));
    visited[r][c] = 0;

    while(!q.empty()) {
        int cr = q.front().r;
        int cc = q.front().c;
        int cpr = q.front().pr;
        int cpc = q.front().pc;
        q.pop();

        for (int i = 0; i < 6; i++) {
            int nr = cr + dr[i];
            int nc = cc + dc[i];
            if (!inRange(nr, nc) || (nr == cpr && nc == cpc) || board[nr][nc] == '-') continue;
            if (visited[nr][nc] >= 0) {
                if ( (visited[nr][nc] + visited[cr][cc])%2 == 0) {
                    ans = max(ans, 3);
                    return;
                }
                continue;
            }
            visited[nr][nc] = visited[cr][cc] + 1;
            q.push(Node(nr, nc, cr, cc));
            ans = max(ans, 2);
        }
    }
}

int main() {
    cin >> N;
    memset(visited, -1, sizeof(visited));
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        board.push_back(s);
    }

    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            if (visited[r][c] >= 0 || board[r][c] != 'X') continue;
            ans = max(ans, 1);
            bfs(r,c);
        }
    }
    cout << ans;
}