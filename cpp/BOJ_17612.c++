#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define ll long long 

struct Cart {
    int n, i;
    ll t;
    Cart(int n, int i, ll t) : n(n), i(i), t(t) {}

    bool operator<(const Cart &other) const {
        if (t == other.t) {
            return i < other.i;
        }
        return t > other.t;
    }
};

int main() { 
    vector<ll> arr;
    priority_queue<Cart> pqCart;
    priority_queue<int, vector<int>, greater<int>> pqIdx;
    ll ans = 0;

    int N,K; cin >> N >> K;
    for (int i=1;i<=K;i++) pqIdx.push(i);

    ll pastTime = 0;

    for (int i=0;i<N;i++) {
        int n, t; cin >> n >> t;
        if (pqIdx.empty()) {
            int popT = pqCart.top().t;
            pastTime = popT;

            while(!pqCart.empty() && pqCart.top().t == popT) {
                int popIdx = pqCart.top().i;
                pqIdx.push(popIdx);
                
                arr.push_back(pqCart.top().n);

                pqCart.pop();
            }
        }
        int idx = pqIdx.top();
        pqIdx.pop();

        pqCart.push(Cart(n, idx, pastTime + t));
    }

    while (!pqCart.empty()) {
        arr.push_back(pqCart.top().n);
        pqCart.pop();
    }
    
    for (int i=1;i<=N;i++) {
        ans += arr[i-1] * i;
    }

    cout << ans;
}