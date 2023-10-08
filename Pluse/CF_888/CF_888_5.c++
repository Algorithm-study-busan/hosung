#include <iostream>
#include <queue>
#include <cstring>
#include <vector>
using namespace std;
#define ll long long
#define MAX 200001
#define INF 987654321

int inDegree[MAX] = {0,};
ll ans[MAX] = {0,};
ll cost[MAX] = {0,};
bool unLimit[MAX] = {0,};
vector<int> edges[MAX];
int N,K;

struct Node {
    int n, c;
    Node(int n, int c) : n(n), c(c) {}
};

void topology() {
    queue<int> q;
    for (int n=1;n<=N;n++) {
        if (inDegree[n] == 0) {
            q.push(n);
            if (unLimit[n]) cost[n] = 0;
            else ans[n] = cost[n];
        }
    }
    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int nxt : edges[cur]) {
            if (unLimit[nxt]) ans[nxt] = 0;
            else ans[nxt] += min(ans[cur], cost[cur]);
            if (--inDegree[nxt] == 0) {
                q.push(nxt);
            }
        }
    }
}

int main() {
    int T; cin >> T;
    while (T--) {
        cin >> N >> K;
        memset(cost, 0, sizeof(cost));
        memset(inDegree, 0, sizeof(inDegree));
        memset(ans, 0, sizeof(ans));
        memset(unLimit, false, sizeof(ans));
        for (int n=1;n<=N;n++) {
            cin >> cost[n];
            edges[n].clear();
        }
        for (int i=0;i<K;i++) {
            int k; cin >> k;
            unLimit[k] = true;
        }

        for (int n=1;n<=N;n++) {
            int m; cin >> m;
            for (int i=0;i<m;i++) {
                int tn; cin >> tn;
                edges[tn].push_back(n);
                inDegree[n]+=1;
            }
        }

        topology();
        for (int n=1;n<=N;n++) {
            cout << min(cost[n], ans[n]) << " ";
        }
        cout << "\n";
    }
}