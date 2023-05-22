#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define MAX 100001

class Log {
    public:
    int n, x1, x2, y;
    Log(int _n, int _x1, int _x2, int _y) {
        n = _n;
        x1 = _x1;
        x2 = _x2;
        y = _y;
    }
};

bool cmp(Log a, Log b) {
    return a.x1 < b.x1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<Log> logArr;
    int N, Q; cin >> N >> Q;
    for (int i=1;i<=N;i++) {
        int x1, x2, y; cin >> x1 >> x2 >> y;
        logArr.push_back(Log(i, x1, x2, y));
    }
    sort(logArr.begin(), logArr.end(), cmp);

    int set[MAX];

    int lastSetIdx = 0;
    int maxX = 0;

    for (Log log : logArr) {
        if (maxX < log.x1) {
            set[log.n] = ++lastSetIdx;
            maxX = log.x2;
        }
        else {
            set[log.n] = lastSetIdx;
            maxX = max(maxX, log.x2);
        }
    }

    for(int i=0;i<Q;i++) {
        int a,b; cin >> a >> b;
        cout << (set[a] == set[b]) << "\n";
    }

}