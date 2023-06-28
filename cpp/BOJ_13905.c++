#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define MAX 100001
#define INF 987654321
int V,E;
vector<pair<int,int>> edges[MAX];
int dist[MAX] = {0,};

struct Node {
    int n, d;
    Node(int n, int d) : n(n), d(d) {}
    bool operator< (const Node &other) const {
        return d < other.d;
    }
};

void dijkstra(int s, int e) {
    priority_queue<Node> pq;
    pq.push(Node(s, INF));
    while(!pq.empty()) {
        int curNode = pq.top().n;
        int curDist = pq.top().d;
        pq.pop();

        if (curDist < dist[curNode]) continue;

        for (int i=0;i<edges[curNode].size();i++) {
            int nextNode = edges[curNode][i].first;
            int nextDist = min(curDist, edges[curNode][i].second);

            if (dist[nextNode] >= nextDist) continue;

            dist[nextNode] = nextDist;
            pq.push(Node(nextNode, nextDist));
        }
    }

    cout << dist[e];
}

int main() {
    cin >> V >> E;
    int s,e; cin >> s >> e;
    for (int i=0;i<E;i++) {
        int a,b,d; cin >> a >> b >> d;
        edges[a].push_back({b,d});
        edges[b].push_back({a,d});   
    }

    dijkstra(s,e);
}   