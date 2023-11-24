#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
#define MAX 100001

vector<int> edges[MAX];
int visitedOrder[MAX]; // -1 로 초기화
bool isSCC[MAX] = {0,};
int SCC_id[MAX] = {0,};
vector<int> stk;
int order = 1;
int id = 1;

void clear(int V) {
    for (int n=1;n<=V;n++) edges[n].clear();
    memset(visitedOrder, -1, sizeof(visitedOrder));
    memset(isSCC, 0, sizeof(isSCC));
    memset(SCC_id, 0, sizeof(SCC_id));
    stk.clear();
    order = 1;
    id = 1;
}

int findSCC(int curNode) {
    visitedOrder[curNode] = order++;
    int minOrder = visitedOrder[curNode];
    stk.push_back(curNode);

    for (int nextNode : edges[curNode]) {
        if (visitedOrder[nextNode] == -1) {
            minOrder = min(minOrder, findSCC(nextNode));
        } else if (!isSCC[nextNode]) {
            minOrder = min(minOrder, visitedOrder[nextNode]);
        }
    }

    if (minOrder == visitedOrder[curNode]) {
        while (true) {
            int x = stk.back();
            stk.pop_back();
            isSCC[x] = true;
            SCC_id[x] = id;
            if (x == curNode) break;
        }
        id++;
    }
    return minOrder;
}

void solve(int V) {
    for (int n=1;n<=V;n++) {
        if (visitedOrder[n] == -1) {
            findSCC(n);
        }
    }

    int SCC_indgree[MAX] = {0,};
    for (int n=1;n<=V;n++) {
        for (int an : edges[n]) {
            if (SCC_id[n] != SCC_id[an]) {
                SCC_indgree[SCC_id[an]] += 1;
            }
        }
    }

    int ret = 0;
    for (int i=1;i<id;i++) {
        ret += (SCC_indgree[i] == 0 ? 1 : 0);
        
    }
    cout << ret << "\n";
}


int main() {
    memset(visitedOrder, -1, sizeof(visitedOrder));
    int T; cin >> T;
    while (T--) {
        int V,E; cin >> V >> E;
        for (int i=0;i<E;i++) {
            int a,b; cin >> a >> b;
            edges[a].push_back(b);
        }
        solve(V);
        clear(V);
    }
}