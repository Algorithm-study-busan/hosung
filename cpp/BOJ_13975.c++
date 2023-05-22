#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define ll long long

struct cmp {
    bool operator()(ll a, ll b) {
        return a > b;
    }
};

int main() {
    int T; cin >> T;
    while (T--) {
        int N; cin >> N;
        priority_queue<ll, vector<ll>, cmp> pq;
        for (int i=0;i<N;i++) {
            ll a; cin >> a;
            pq.push(a);
        }

        ll ans = 0;
        while(pq.size() > 1) {
            ll x = 0;
            x += pq.top();
            pq.pop();
            x += pq.top();
            pq.pop();

            pq.push(x);
            ans += x;
        }

        cout << ans << '\n';
    }
}