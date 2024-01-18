#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;
int V,E,S,K;
vector<int> edges[1001];
set<int> ans;
bool visited[1001][1001] = {0,};

void bfs(int s) {
    queue<pair<int,int>> q;
    q.push({s, 0});
    visited[s][0] = true;

    while (!q.empty()) {
        int curNode = q.front().first;
        int curK = q.front().second;
        q.pop();

        if (edges[curNode].empty()) return;
        if (curK == K) {
            ans.insert(curNode);
            continue;
        }

        for (int nextNode : edges[curNode]) {
            if (visited[nextNode][curK+1]) continue;
            visited[nextNode][curK+1] = true;
            q.push({nextNode, curK+1});
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> V >> E >> S >> K;
    for (int i=0;i<E;i++) {
        int a,b; cin >> a >> b;
        edges[a].push_back(b);
        edges[b].push_back(a);
    }
    bfs(S);

    if (ans.empty()) cout << -1;
    else {
        for (int x : ans) cout << x << " ";
    }
}