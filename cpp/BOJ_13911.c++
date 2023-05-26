#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MAX 100001
#define INF 987654321
int V,E,M,X,S,Y;
vector<pair<int,int>> edges[MAX];
vector<int> distMc, distSt;

void dijkstra(priority_queue<pair<int,int>> pq, vector<int> &dist) {
    while(!pq.empty()) {
        int curDist = -pq.top().first;
        int curNode = pq.top().second;
        pq.pop();

        if (dist[curNode] < curDist) continue;

        for (int i=0;i<edges[curNode].size();i++) {
            int nextDist = curDist + edges[curNode][i].second;
            int nextNode = edges[curNode][i].first;

            if (dist[nextNode] <= nextDist) continue;
            dist[nextNode] = nextDist;
            pq.push({-nextDist, nextNode});
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> V >> E;
    for (int i=0;i<E;i++) {
        int a,b,c; cin >> a >> b >> c;
        edges[a].push_back({b,c});
        edges[b].push_back({a,c});
    }
    for (int i=0;i<V+1;i++) {
        distMc.push_back(INF);
        distSt.push_back(INF);
    }
    
    cin >> M >> X;
    priority_queue<pair<int,int>> pqMc, pqSt;
    for(int i=0;i<M;i++) {
        int m; cin >> m;
        distMc[m] = 0;
        pqMc.push({0,m});
    }
    dijkstra(pqMc, distMc);

    cin >> S >> Y;
    for(int i=0;i<S;i++) {
        int s; cin >> s;
        distSt[s] = 0;
        pqSt.push({0,s});
    }
    dijkstra(pqSt, distSt);

    int ans = INF;
    for(int v=1;v<=V;v++) {
        if (distMc[v] == 0 || distSt[v] == 0
            || distMc[v] > X || distSt[v] > Y) continue;
        ans = min(ans, distMc[v] + distSt[v]);
    }
    cout << (ans == INF ? -1 : ans);
}