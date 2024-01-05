#include <iostream>
#include <vector>
#include <string>
#include <queue> 
using namespace std;
#define MAX 20100
#define INF 987654321 

struct Edge {
    int from, to, cap, flow;
    Edge* reverse;

    Edge(int from, int to, int cap, int flow) : from(from), to(to), cap(cap), flow(flow) {}

    int residual() {
        return cap - flow;
    }
};

int R,C;
vector<string> board;
int dr[] = {-1,0,1,0};
int dc[] = {0,-1,0,1};
vector<Edge*> edges[MAX];

bool inRange(int r, int c) {
    return r >= 0 && r < R && c >= 0 && c < C;
}

int map(int r, int c) {
    return r*C + c;
}


int networkFlow(int s, int e) {
    int totalFlow = 0;

    while (1) {
        vector<Edge*> parent(MAX, nullptr);

        queue<int> q;
        q.push(s);

        while(!q.empty() && parent[e] == nullptr) {
            int cur = q.front();
            q.pop();

            for (Edge* edge : edges[cur]) {                
                if (edge->residual() > 0 && parent[edge->to] == nullptr) {
                    q.push(edge->to);
                    parent[edge->to] = edge;
                }
            }
        }

        if (parent[e] == nullptr) break;

        int curFlow = 1;
        for (int p=e;p!=s;p=parent[p]->from) {
            parent[p]->flow += curFlow;
            parent[p]->reverse->flow -= curFlow;
        }

        totalFlow += curFlow;
    }
    return totalFlow;
}

void solve(int sr, int sc, int er, int ec) {
    for (int i=0;i<4;i++) {
        if (sr + dr[i] == er && sc + dc[i] == ec) {
            cout << -1;
            return;
        }
    }
    cout << networkFlow(map(sr,sc)*2, map(er,ec)*2+1);
}

int main() {
    cin >> R >> C;
    for (int i=0;i<R;i++) {
        string s; cin >> s;
        board.push_back(s);
    }

    int sr,sc, er,ec;

    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            if (board[r][c] == 'K') {
                sr = r;
                sc = c;
            } else if (board[r][c] == 'H') {
                er = r;
                ec = c;
            } else if (board[r][c] == '#') continue;

            for (int i=0;i<4;i++){
                int nr = r+dr[i];
                int nc = c+dc[i];
                if (inRange(nr,nc) && board[nr][nc] != '#') {
                    Edge *edge = new Edge(map(r,c)*2+1, map(nr,nc)*2, 1, 0);
                    Edge *reverseEdge = new Edge(map(nr, nc)*2, map(r,c)*2+1, 0, 0);
                    edge->reverse = reverseEdge;
                    reverseEdge->reverse = edge;
                    edges[map(r,c)*2+1].push_back(edge);
                    edges[map(nr,nc)*2].push_back(reverseEdge);
                }
            }
        }
    }


    for (int i=0;i<R*C;i++) {
        Edge *edge = new Edge(i*2, i*2+1, 1, 0);
        Edge *reverseEdge = new Edge(i*2+1, i*2, 0, 0);
        if (i == map(sr,sc) || i == map(er,ec)) {
            edge->cap = INF;
        } 
        edge->reverse = reverseEdge;
        reverseEdge->reverse = edge;
        
        edges[i*2].push_back(edge);
        edges[i*2+1].push_back(reverseEdge);
    }

    solve(sr, sc, er, ec);
}