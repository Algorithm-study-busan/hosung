#include <iostream>
#include <vector>
#include <queue> 
using namespace std;
#define MAX 210
#define INF 987654321

int cap[MAX][MAX] = {0,};
int flow[MAX][MAX] = {0,};
int cost[MAX][MAX] = {0,};

void MCMF(int s, int e) {
    int totalFlow = 0;
    int totalCost = 0;

    while (1) {
        priority_queue<pair<int,int>> pq;
        pq.push({0, s});

        vector<int> parent(MAX, -1);
        parent[s] = s;

        vector<int> dist(MAX, INF);
        dist[s] = 0;

        while (!pq.empty()) {
            int cur = pq.top().second;
            int curDist = -pq.top().first;
            pq.pop();

            for (int next=1;next<MAX;next++) {
                int nextDist = curDist + cost[cur][next];
                if (cap[cur][next] - flow[cur][next] > 0 && dist[next] > nextDist) {
                    dist[next] = nextDist;
                    parent[next] = cur;
                    pq.push({-nextDist, next});
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
            totalCost += cost[parent[p]][p] * curFlow;
        }

        totalFlow += curFlow;
    }
    cout << totalFlow << "\n" << totalCost;
}

int main() {
    int N,M; cin >> N >> M;
    for (int n=M+1;n<=N+M;n++) {
        cin >> cap[n][N+M+1];
    }
    for (int m=1;m<=M;m++) {
        cin >> cap[0][m];
    }
    for (int m=1;m<=M;m++) {
        for (int n=M+1;n<=N+M;n++) {
            cin >> cap[m][n];
        }
    }
    for (int m=1;m<=M;m++) {
        for (int n=M+1;n<=N+M;n++) {
            int c; cin >> c;
            cost[m][n] = c;
            cost[n][m] = -c;
        }
    }
    MCMF(0, N+M+1);
}