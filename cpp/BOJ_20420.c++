#include <iostream>
#include <vector> 
#include <queue>
#include <string>
using namespace std;
int R,C,K;
vector<string> board;

struct Node {
    int r,c, cntL, cntR;
    Node(int r, int c, int cntL, int cntR) : r(r), c(c), cntL(cntL), cntR(cntR){}
};

int drl[] = {-1,0,1,0};
int dcl[] = {0,-1,0,1};

int drr[] = {-1,0,1,0};
int dcr[] = {0,1,0,-1};

int mapRightIdx(char c) {
    if (c == 'U') return 0; 
    else if (c == 'R') return 1;
    else if (c == 'D') return 2;
    else return 3;
}

int mapLeftIdx(char c) {
    if (c == 'U') return 0;
    else if (c == 'L') return 1;
    else if (c == 'D') return 2;
    else return 3;
}

int calCnt(int curIdx, int toIdx) {
    int ret = toIdx - curIdx;
    if (ret < 0) return ret + 4;
    return ret;
}

bool inRange(int r, int c) {
    return r>=0 && r<R && c>=0 && c<C;
}

bool bfs() {
    bool visited[50][50][151][151] = {0,};
    visited[0][0][0][0] = true;
    queue<Node> q;
    q.push(Node(0,0,0,0));

    while(!q.empty()) {
        int cr = q.front().r;
        int cc = q.front().c;
        int curCntL = q.front().cntL;
        int curCntR = q.front().cntR;
        q.pop();

        if (cr == R-1 && cc == C-1) return true;

        for (int i=0;i<4;i++) {
            int nr = cr + drr[i];
            int nc = cc + dcr[i];
            int nxtCntR = curCntR + calCnt(mapRightIdx(board[cr][cc]), i);

            if (inRange(nr, nc) && nxtCntR <= K && !visited[nr][nc][curCntL][nxtCntR]) {
                visited[nr][nc][curCntL][nxtCntR] = true;
                q.push(Node(nr, nc, curCntL, nxtCntR));
            }
        }

        for (int i=0;i<4;i++) {
            int nr = cr + drl[i];
            int nc = cc + dcl[i];
            int nxtCntL = curCntL + calCnt(mapLeftIdx(board[cr][cc]), i);

            if (inRange(nr, nc) && nxtCntL <= K && !visited[nr][nc][nxtCntL][curCntR]) { 
                visited[nr][nc][nxtCntL][curCntR] = true;
                q.push(Node(nr, nc, nxtCntL, curCntR));
            }
        }

    }
    return false; 
}

int main() {
    cin >> R >> C >> K;
    for (int i=0;i<R;i++) {
        string s; cin >> s; 
        board.push_back(s);
    }
    cout << (bfs() ? "Yes" : "No");
}