#include <iostream>
using namespace std;
#define MAX 100001
int parent[MAX] = {0,};
int ans[MAX] = {0,};

int main() {
    int N, M; cin >> N >> M;
    for(int n=1;n<=N;n++) {
        cin >> parent[n];
    }
    for(int i=0;i<M;i++) {
        int a,b; cin >> a >> b;
        ans[a] += b;
    }
    for (int n=1;n<=N;n++) {
        ans[n] += ans[parent[n]];
    }
    for (int n=1;n<=N;n++) {
        cout << ans[n] << " ";
    }
}