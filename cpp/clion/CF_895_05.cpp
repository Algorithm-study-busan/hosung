#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#define MAX 100001

using namespace std;
int arr[MAX] = {0,};
int inDegree[MAX] = {0,};
vector< pair<int,int> > cost;
vector<int> ans;
int N;

void topologySort(queue<int> &q) {
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (--inDegree[arr[cur]] == 0) {
            ans.push_back(arr[cur]);
            q.push(arr[cur]);
        }
    }
    queue<int> nextQ;
    if (ans.size() != N) {
        for (auto p: cost) {
            if (inDegree[arr[p.second]]-1 == 0) {
                inDegree[arr[p.second]] -= 1;
                nextQ.push(arr[p.second]);
                ans.push_back(arr[p.second]);
                topologySort(nextQ);
            }
        }
    }
}

int main() {
    int T; cin >> T;
    while (T--) {
        memset(arr, 0, sizeof(arr));
        memset(inDegree, 0, sizeof(inDegree));
        cost.clear();
        ans.clear();
        cin >> N;
        for (int i = 1; i <= N; i++) {
            cin >> arr[i];
            inDegree[arr[i]] += 1;
        }
        for (int i = 0; i < N; i++) {
            int c; cin >> c;
            cost.push_back(make_pair(c, i + 1));
        }

        sort(cost.begin(), cost.end());
        queue<int> q;
        for (int n = 1; n <= N; n++) {
            if (inDegree[n] == 0) {
                ans.push_back(n);
                q.push(n);
            }
        }
        topologySort(q);
        for (int x : ans) cout << x << " ";
        cout << "\n";
    }
}