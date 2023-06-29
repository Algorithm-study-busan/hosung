#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MOD 1000000007
#define ll long long

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int T; cin >> T;
    while (T--) {
        int N; cin >> N;

        priority_queue<ll, vector<ll>, greater<ll>> pq;
        ll ans = 1;

        for (int i=0;i<N;i++) {
            ll x; cin >> x;
            pq.push(x);
        }  

        while (pq.size() > 1) { 
            ll a = pq.top();
            pq.pop();
            ll b = pq.top();
            pq.pop();

            ans *= a*b % MOD;
            ans %= MOD;
            pq.push(a*b);
        }

        cout << ans << '\n';
    }
}