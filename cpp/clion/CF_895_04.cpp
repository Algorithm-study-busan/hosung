#include <iostream>
#define ll long long
using namespace std;

ll lcm(ll a, ll b) {
    ll ta = a;
    ll tb = b;
    ll c = a % b;
    while (c) {
        a = b;
        b = c;
        c = a % b;
    }
    return ta * tb / b;
}

int main() {
    int T; cin >> T;
    while (T--) {
        ll n, x, y; cin >> n >> x >> y;
        ll k = lcm(x, y);
        ll cntX = n / x - n / k;
        ll cntY = n / y - n / k;

        ll retX = (n + n - cntX +1) * cntX / 2;
        ll retY = cntY * (cntY + 1) / 2;
        cout << retX - retY << "\n";
    }
}