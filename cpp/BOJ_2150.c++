#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
#define MAX 10001

int V,E;
vector<int> edges[MAX];
vector<int> stk;
int visitedOrder[MAX]; // -1 로 할당
bool isScc[MAX] = {0,};
vector<vector<int>> sccs;

int order = 0;

int findSCC(int curNode) {
    visitedOrder[curNode] = ++order;
    int minOrder = visitedOrder[curNode];
    stk.push_back(curNode);

    for (int nextNode : edges[curNode]) {
        if (visitedOrder[nextNode] == -1) {
            minOrder = min(minOrder, findSCC(nextNode));
        }
        else if (!isScc[nextNode]) {
            minOrder = min(minOrder, visitedOrder[nextNode]);
        }
    }

    if (minOrder == visitedOrder[curNode]) {
        vector<int> scc;
        while (true) {
            int x = stk.back();
            stk.pop_back();
            isScc[x] = true;
            scc.push_back(x);
            if (x == curNode) break;
        }
        sccs.push_back(scc);
    }
    return minOrder;
}

bool cmp(const vector<int> &a, const vector<int> &b) {
    return a.front() < b.front();
}

int main() {
    cin >> V >> E;
    for (int i=0;i<E;i++) {
        int a,b; cin >> a >> b;
        edges[a].push_back(b);
    }

    memset(visitedOrder, -1, sizeof(visitedOrder));
    for (int n=1;n<=V;n++) {
        if (visitedOrder[n] == -1) {
            findSCC(n);
        }
    }

    cout << sccs.size() << '\n';
    for (auto &scc : sccs) {
        sort(scc.begin(), scc.end());
    }

    sort(sccs.begin(), sccs.end(), cmp);

    for (auto &scc : sccs) {
        for (auto x : scc) {
            cout << x << " ";
        }
        cout << "-1\n";
    }
}