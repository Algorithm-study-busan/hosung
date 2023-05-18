#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 100001
int N;
vector<int> edges[MAX];
vector<int> arr;
vector<int> ans;
int order[MAX] = {0,};
bool visited[MAX] = {0,};

bool cmp(int a, int b) {
    return order[a] < order[b];
}

void dfs(int cur) {
    if (visited[cur]) return;
    visited[cur] = true;
    ans.push_back(cur);

    for (int nxt : edges[cur]) {
        dfs(nxt);
    }
}


int main() {
    cin >> N;
    for (int i=0;i<N-1;i++) {
        int a,b; cin >> a >> b;
        edges[a].push_back(b);
        edges[b].push_back(a);
    }
    for (int i=0;i<N;i++) {
        int a; cin >> a;
        arr.push_back(a);
        order[a] = i;
    }

    for(int i=1;i<=N;i++) {
        sort(edges[i].begin(), edges[i].end(), cmp);
    }

    dfs(1);

    cout << (arr == ans);   
}