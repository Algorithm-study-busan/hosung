#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;
vector<string> board;
struct Node {
    int r, c, cnt;
    Node(int r, int c, int cnt) : r(r), c(c), cnt(cnt) {}
};

int R,C;
int dr[] = {-1,-1,-1,0,1,1,1,0};
int dc[] = {-1,0,1,1,1,0,-1,-1};
int visited[1000][1000] = {0,};

bool inRange(int r, int c) {
    return r>=0 && r<R && c>=0 && c<C;
}

bool check(int r, int c, int v) {
    int cur = board[r][c]-'0';
    int cnt = 0;
    for (int i = 0; i < 8; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (!inRange(nr, nc)) continue;
        if (board[nr][nc] == '.' && visited[nr][nc] < v) cnt += 1;
    }
    return cur <= cnt;
}

void bfs() {
    int ans = 0;
    queue<Node> q;

    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            if (board[r][c] != '.' && check(r,c, 1)) {
                q.push(Node(r,c,1));
                board[r][c] = '.';
                visited[r][c] = 1;
            }
        }
    }


    while (!q.empty()) {
        int cr = q.front().r;
        int cc = q.front().c;
        int ccnt = q.front().cnt;
        q.pop();
        ans = max(ans, ccnt);

        for (int i=0;i<8;i++) {
            int nr = cr + dr[i];
            int nc = cc + dc[i];
            int ncnt = ccnt+1;

            if (!inRange(nr, nc) || board[nr][nc] == '.') continue;
            if (check(nr, nc, ncnt)) {
                q.push(Node(nr, nc, ncnt));
                board[nr][nc] = '.';
                visited[nr][nc] = visited[cr][cc] + 1;
            }
        }
    }
    cout << ans;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> R >> C;
    for (int r=0;r<R;r++) {
        string s; cin >> s;
        board.push_back(s);
    }
    bfs();
}