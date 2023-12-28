#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define MAX 210
#define INF 987654321

int cap[MAX][MAX] = {0,};
int flow[MAX][MAX] = {0,};
int N,M;

int networkFlow(int s, int e) {
    int totalFlow = 0;
    while (1) {
        vector<int> parent(MAX, -1);
        parent[s] = s;

        queue<int> q;
        q.push(s);
        
        while (!q.empty() && parent[e] == -1) {
            int cur = q.front();
            q.pop();
            for (int next = 0; next <= N+M+1; next++) {
                if (cap[cur][next] - flow[cur][next] > 0 && parent[next] == -1) {
                    parent[next] = cur;
                    q.push(next);
                }
            }
        }

        if (parent[e] == -1) break;

        int curFlow = INF;
        for (int p = e; p != s; p = parent[p]) {
            curFlow = min(curFlow, cap[parent[p]][p] - flow[parent[p]][p]);
        }
        for (int p = e; p != s; p = parent[p]) {
            flow[parent[p]][p] += curFlow;
            flow[p][parent[p]] -= curFlow;
        }
        totalFlow += curFlow;
    }
    return totalFlow;
}

int main() {
    cin >> N >> M;
    for (int j=M+1;j<=N+M;j++) {
        cin >> cap[j][N+M+1];
    }
    for (int i=1;i<=M;i++) {
        cin >> cap[0][i];
    }
    for (int i=1;i<=M;i++) {
        for (int j=1+M;j<=N+M;j++) {
            cin >> cap[i][j];
        }
    }

    cout << networkFlow(0, N+M+1);
}