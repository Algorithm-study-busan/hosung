#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MAX 1000
#define INF 987654321
vector<pair<int,int>> edges[MAX];
int dist[MAX] = {0,};

void bfs(int start) {
    queue<pair<int,int>> q;
    q.push({start, INF});
    
    while(!q.empty()) {
        int curNode = q.front().first;
        int curDist = q.front().second;
        q.pop();

        if (dist[curNode] > curDist) continue;

        for (int i=0;i<edges[curNode].size();i++) {
            int nextNode = edges[curNode][i].first;
            int nextDist = min(curDist, edges[curNode][i].second);
            
            if (dist[nextNode] >= nextDist) continue;
            dist[nextNode] = nextDist;
            q.push({nextNode, nextDist});
        }
    }
}

int main() {
    int V,E; cin >> V >> E;
    int start, end; cin >> start >> end;
    for (int i=0;i<E;i++) {
        int a,b,c; cin >> a >> b >> c;
        edges[a].push_back({b,c});
        edges[b].push_back({a,c});
    }

    bfs(start);

    cout << dist[end];
}