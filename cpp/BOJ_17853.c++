#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MAX 100001
#define INF 98765432100
#define ll long long 

vector<pair<int,int>> edges[MAX];
vector<ll> dist(MAX, INF);

void dijkstra(priority_queue<pair<ll,int>> &pq) {
    while(!pq.empty()) {
        int curNode = pq.top().second;
        ll curDist = -pq.top().first;
        pq.pop();

        if (dist[curNode] < curDist) continue;

        for (auto p : edges[curNode]) {
            int nextNode = p.first;
            ll nextDist = curDist + p.second;

            if (dist[nextNode] > nextDist) {
                dist[nextNode] = nextDist;
                pq.push({-nextDist, nextNode});
            }
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int V,E,K; cin >> V >> E >> K;
    for (int i=0;i<E;i++) {
        int a,b,c; cin >> a >> b >> c;
        edges[b].push_back({a,c});
    }

    priority_queue<pair<ll,int>> pq;
    for (int i=0;i<K;i++) {
        int s; cin >> s;
        dist[s] = 0;
        pq.push({0,s});
    }

    dijkstra(pq);

    int ansNode = -1;
    ll ansDist = -1;

    for (int n=1;n<=V;n++) {
        if (ansDist < dist[n]) {
            ansNode = n;
            ansDist = dist[n];
        }
    }
    cout << ansNode << "\n" << ansDist;
}