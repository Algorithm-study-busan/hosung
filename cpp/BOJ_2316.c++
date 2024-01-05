#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MAX 810
#define INF 987654321

int cap[MAX][MAX] = {0,}; 
int flow[MAX][MAX] = {0,};

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

            for (int next=0; next<MAX;next++) {
                if (cap[cur][next] - flow[cur][next] > 0 && parent[next] == -1) {
                    parent[next] = cur;
                    q.push(next);
                }
            }
        }

        if (parent[e] == -1) break;

        int curFlow = INF;
        for (int p=e;p!=s;p=parent[p]) {
            curFlow = min(curFlow, cap[parent[p]][p] - flow[parent[p]][p]);
        }

        for (int p=e;p!=s;p=parent[p]) {
            flow[parent[p]][p] += curFlow;
            flow[p][parent[p]] -= curFlow;
        }
        totalFlow += curFlow;
    }

    return totalFlow;
}

int main() {
    int V,E; cin >> V >> E;

    for (int i=1;i<=V;i++) {
        cap[i*2][i*2+1] = 1;
    }
    cap[2][3] = INF;
    cap[4][5] = INF;

    for (int i=0;i<E;i++) {
        int a, b; cin >> a >> b;
        cap[a*2+1][b*2] = 1;
        cap[b*2+1][a*2] = 1;
    }

    cout << networkFlow(2, 5);
}