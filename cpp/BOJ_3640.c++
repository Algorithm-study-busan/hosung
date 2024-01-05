#include <iostream>
#include <queue>
#include <vector> 
#include <cstring>
using namespace std;
#define MAX 2200
#define INF 987654321
int cap[MAX][MAX] = {0,};
int flow[MAX][MAX] = {0,};
int cost[MAX][MAX] = {0,};

int MCMF(int s, int e) {
    int totalCost = 0;

    while(1) {
        priority_queue<pair<int,int>> pq;
        pq.push({0,s});

        vector<int> dist(MAX, INF);
        dist[s] = 0;

        vector<int> parent(MAX, -1);
        parent[s] = s;

        while (!pq.empty()) {
            int cur = pq.top().second;
            int curDist = -pq.top().first;
            pq.pop();

            for (int next=0;next<MAX;next++) {
                int nextDist;
                nextDist = curDist + cost[cur][next];
                 
                if (cap[cur][next] - flow[cur][next] > 0 && dist[next] > nextDist) {
                    dist[next] = nextDist;
                    pq.push({-nextDist, next});
                    parent[next] = cur;
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
            totalCost += curFlow * cost[parent[p]][p];
        }
    }
    return totalCost;
}

int main() {
    int V,E;
    while (cin >> V >> E) {
        memset(cap, 0, sizeof(cap));
        memset(flow, 0, sizeof(flow));
        memset(cost, 0, sizeof(cost));

        for (int i=1;i<=V;i++) {
            cap[i*2][i*2+1] = 1;
        }
        cap[2][3] = 2;
        cap[V*2][V*2+1] = 2;
        

        for (int i=0;i<E;i++) {
            int a,b,c; cin >> a >> b >> c;
            cap[a*2+1][b*2] = 1;
            cost[a*2+1][b*2] = c;
            cost[b*2][a*2+1] = -c;
        }
        cout << MCMF(2, V*2+1) << "\n";
    }
};