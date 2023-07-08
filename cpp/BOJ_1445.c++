#include <iostream>
#include <queue>
#include <vector> 
#include <string>
using namespace std; 
#define MAX 50
#define INF 987654321
int R,C, sr,sc, fr,fc;
int dr[] = {-1,0,1,0};
int dc[] = {0,-1,0,1};
vector<string> board;
pair<int,int> visited[MAX][MAX];

struct Node {
    int r,c,g,ng;
    Node(int r, int c, int g, int ng) : r(r), c(c), g(g), ng(ng) {}
};

bool inRange(int r, int c) {
    return r>=0 && r<R && c>=0 && c<C;
}

bool nearGarbage(int r, int c) {
    for (int i=0;i<4;i++) {
        int nr = r+dr[i];
        int nc = c+dc[i];
        if (inRange(nr,nc) && board[nr][nc] == 'g') {
            return true;
        }
    }
    return false;
}

void bfs() {
    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            visited[r][c] = make_pair(INF, INF);
        }
    }
    queue<Node> q;
    visited[sr][sc] = make_pair(0, 0);
    q.push(Node(sr,sc,0,0));

    while(!q.empty()) {
        Node curNode = q.front();
        q.pop();

        for (int i=0;i<4;i++) {
            int nr = curNode.r + dr[i];
            int nc = curNode.c + dc[i];
            if (!inRange(nr,nc)) continue;

            int ng = curNode.g + (board[nr][nc] == 'g' ? 1 : 0);
            int nng = curNode.ng + (board[nr][nc] == '.' ? nearGarbage(nr,nc) : 0);


            // cout << nr << " " << nc << " " << ng << " " << nng << endl;

            if (visited[nr][nc].first < ng) continue;
            else if (visited[nr][nc].first > ng) {
                visited[nr][nc] = make_pair(ng, nng);
                q.push(Node(nr,nc,ng,nng));
            }
            else {
                if (visited[nr][nc].second <= nng) continue;
                else {
                    visited[nr][nc] = make_pair(ng, nng);
                    q.push(Node(nr,nc,ng,nng));
                }
            }
        }
    }

    cout << visited[fr][fc].first << " " << visited[fr][fc].second << endl;
}

int main() {
    cin >> R >> C;
    for (int i=0;i<R;i++) {
        string s; cin >> s;
        board.push_back(s);
    }

    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            if (board[r][c] == 'S') {
                sr=r;
                sc=c;
            }
            if (board[r][c] == 'F') {
                fr=r;
                fc=c;
            }
        }
    }

    bfs();

    // for (int r=0;r<R;r++) {
    //     for (int c=0;c<C;c++) {
    //         cout << visited[r][c].first << ":" << visited[r][c].second << " ";
    //     }
    //     cout << endl;
    // }
}