#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define INF 987654321
int board[5][5][5] = {0, };
int dk[] = {-1,1,0,0,0,0};
int dr[] = {0,0,-1,0,1,0};
int dc[] = {0,0,0,-1,0,1};
int ans = INF;

struct Node {
    int k,r,c;
    Node(int k, int r, int c) : k(k), r(r), c(c) {}
};

bool inRange(int k, int r, int c) {
    return k>=0 && k<5 && r>=0 && r<5 && c>=0 && c<5;
}

int bfs(int cube[5][5][5]) {
    if (cube[0][0][0] == 0) return INF;
    int visited[5][5][5];
    for (int k=0;k<5;k++){
        for (int r=0;r<5;r++) {
            for (int c=0;c<5;c++) {
                visited[k][r][c] = -1;
            }
        }
    }
    queue<Node> q;
    q.push(Node(0, 0, 0));
    visited[0][0][0] = 0;
    while (!q.empty()) {
        int ck = q.front().k;
        int cr = q.front().r;
        int cc = q.front().c;
        q.pop();

        if (ck == 4 && cr == 4 && cc == 4) return visited[ck][cr][cc];

        for (int i = 0; i < 6; i++) {
            int nk = ck + dk[i];
            int nr = cr + dr[i];
            int nc = cc + dc[i];

            if (!inRange(nk, nr, nc) || cube[nk][nr][nc] == 0 || visited[nk][nr][nc] != -1) continue;
            q.push(Node(nk, nr, nc));
            visited[nk][nr][nc] = visited[ck][cr][cc] + 1;
        }
    }
    return INF;
}

void rotate(int k) {
    int tmp[5][5] = {0,};
    for (int r=0;r<5;r++) {
        for (int c=0;c<5;c++) {
            tmp[r][c] = board[k][4-c][r];
        }
    }
    for (int r=0;r<5;r++) {
        for (int c=0;c<5;c++) {
            board[k][r][c] = tmp[r][c];
        }
    }
}

void dfs(int k) {
    if (k == 5) {
        vector<int> arr;
        for (int i = 0; i < 5; i++) arr.push_back(i);
        do {
            int cube[5][5][5] = {0,};
            for (int i=0;i<5;i++) {
                for (int r=0;r<5;r++) {
                    for (int c=0;c<5;c++) {
                        cube[i][r][c] = board[arr[i]][r][c];
                    }
                }
            }
            ans = min(ans, bfs(cube));
        } while (next_permutation(arr.begin(), arr.end()));
        return;
    }

    for (int i=0;i<4;i++) {
        dfs(k+1);
        rotate(k);
    }
}

int main() {
    for (int k = 0; k < 5; k++) {
        for (int r = 0; r < 5; r++) {
            for (int c = 0; c < 5; c++) {
                cin >> board[k][r][c];
            }
        }
    }

    dfs(0);
    cout << (ans == INF ? -1 : ans);
}