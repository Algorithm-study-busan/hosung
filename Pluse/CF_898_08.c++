#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;
#define MAX 200001

vector<int> edges[MAX];
int inDegree[MAX] = {0,};
int dist_M[MAX];
int dist_V[MAX];

void checkCycle(int N) {
    queue<int> q;
    for (int n=1;n<=N;n++) {
        if (inDegree[n] == 1) {
            q.push(n);
        }
    }
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        for (int nxt : edges[cur]) {
            if (--inDegree[nxt] == 1) q.push(nxt);
        }
    }
}

void distToCycle(int n, int dist[MAX]) {
    queue<int> q;
    q.push(n);
    dist[n] = 0;

    while (!q.empty()) {
        int curNode = q.front();
        q.pop();

        for (int nextNode : edges[curNode]) {
            if (dist[nextNode] != -1) continue;
            dist[nextNode] = dist[curNode] + 1;
            q.push(nextNode);
        }
    }
}

void solve(int N) { 
    for (int n=1;n<=N;n++) {
        if (inDegree[n] == 2 && dist_M[n] > dist_V[n]) {
            cout << "YES\n";
            return;
        }
    }
    cout << "NO\n";
}


int main() {
    int T; cin >> T;
    while (T--) {
        int N,M,V; cin >> N >> M >> V;
        for (int i=0;i<=N;i++) edges[i].clear();
        memset(inDegree, 0, sizeof(inDegree));
        memset(dist_M, -1, sizeof(dist_M));
        memset(dist_V, -1, sizeof(dist_V));
        

        for (int i=0;i<N;i++) {
            int a, b; cin >> a >> b;
            edges[a].push_back(b);
            edges[b].push_back(a);
            inDegree[a]++;
            inDegree[b]++;
        }
        checkCycle(N);
        distToCycle(M, dist_M);
        distToCycle(V, dist_V);

        solve(N);
    }
}