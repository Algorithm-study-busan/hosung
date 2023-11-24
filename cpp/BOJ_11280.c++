#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
#define MAX 25000
vector<int> edges[MAX];
vector<vector<int>> sccs;
bool isSCC[MAX] = {0,};
int visitedOrder[MAX]; // -1
int order = 0;
vector<int> stk;

int mapNode(int n) {
    if (n>0) return n;
    return MAX + n;
}

int findSCC(int curNode) {
    visitedOrder[curNode] = ++order;
    int minOrder = visitedOrder[curNode];
    stk.push_back(curNode);

    for(int nextNode : edges[curNode]) {
        if (visitedOrder[nextNode] == -1) {
            minOrder = min(minOrder, findSCC(nextNode));
        } else if (!isSCC[nextNode]) {
            minOrder = min(minOrder, visitedOrder[nextNode]);
        }
    }

    if (minOrder == visitedOrder[curNode]) {
        vector<int> scc;
        while (true) {
            int x = stk.back();
            stk.pop_back();
            scc.push_back(x);
            isSCC[x] = true;
            if (x == curNode) break;
        }
        sccs.push_back(scc);
    }
    return minOrder;
}

int solve() {
    for(auto scc : sccs) {
        bool set[MAX] = {0,};
        for (int x : scc) {
            if (x > 10000) x = MAX - x;
            if (set[x]) return 0;
            set[x] = true;
        }
    }
    return 1;
}

int main() { 
    memset(visitedOrder, -1, sizeof(visitedOrder));
    int V, E; cin >> V >> E;
    for(int i=0;i<E;i++) {
        int a,b; cin >> a >> b;
        edges[mapNode(-a)].push_back(mapNode(b));
        edges[mapNode(-b)].push_back(mapNode(a));
    }

    for (int n=1;n<=V;n++) {
        if (visitedOrder[n] == -1) {
            findSCC(n);
        }
    }
    for (int n=-1;n>=-V;n--) {
        if (visitedOrder[mapNode(n)] == -1) {
            findSCC(mapNode(n));
        }
    }

    cout << solve();
}   