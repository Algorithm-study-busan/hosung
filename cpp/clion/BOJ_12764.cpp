#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define MAX 100001
int cnt[MAX] = {0,};
int sitArr[MAX] = {0,};

struct Node {
    bool start;
    int time, n;
    Node(bool start, int time, int n ) : start(start), time(time), n(n) {}

    bool operator<(const Node &other) const {
        return time < other.time;
    }
};

int main_12764() {
    int N; cin >> N;
    vector<Node> arr;
    for (int i=0;i<N;i++) {
        int s,e; cin >> s >> e;
        arr.push_back(Node(true, s, i));
        arr.push_back(Node(false, e, i));
    }

    sort(arr.begin(), arr.end());

    priority_queue<int, vector<int>, greater<int>> pq;
    for(int n=1;n<=N;n++) {
        pq.push(n);
    }

    int ans = 0;
    int tmp = 0;
    for (Node node : arr) {
        if (node.start) {
            int sit = pq.top();
            pq.pop();

            cnt[sit]++;
            sitArr[node.n] = sit;

            tmp++;
            ans = max(ans, tmp);
        }

        else {
            pq.push(sitArr[node.n]);
            tmp--;
        }
    }

    cout << ans << "\n";
    for (int i=1;i<=ans;i++) {
        cout << cnt[i] << " ";
    }
}