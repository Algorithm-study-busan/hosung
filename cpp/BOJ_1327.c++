#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;
#define INF 987654321

int N,K;

bool isAscending(const string &arr) {
    for (int i=1;i<N;i++) {
        if (arr[i-1] > arr[i]) return false;
    }
    return true;
}

void bfs(string arr) {
    map<string, bool> visited;
    queue<pair<string, int>> q;
    q.push({arr,0});
    visited[arr] = true;

    while(!q.empty()) {
        string curArr = q.front().first;
        int curCnt = q.front().second;
        q.pop();

        if (isAscending(curArr)) {
            cout << curCnt;
            return;
        }

        for (int i=0;i<=N-K;i++) {
            reverse(curArr.begin() + i, curArr.begin() + i + K);
            if (visited[curArr]) {
                reverse(curArr.begin() + i, curArr.begin() + i + K);
                continue;
            }

            q.push({curArr, curCnt+1});
            visited[curArr] = true;
            reverse(curArr.begin() + i, curArr.begin() + i + K);
        }
    }
    cout << -1;
    return;
}

int main() {
    cin >> N >> K;
    string arr;
    for (int i=0;i<N;i++) {
        int x; cin >> x;
        arr.push_back(x);
    }

    bfs(arr);
}