#include <iostream>
#include <map>
#define ll long long
using namespace std;
int N,K; 

int main() {
    cin >> N >> K;
    map<ll,ll> count;
    ll sum = 0;
    ll ans = 0;
    for (int i=0;i<N;i++) {
        int x; cin >> x;
        sum += x;
        count[sum] += 1;
        ans += count[K]
    }
}