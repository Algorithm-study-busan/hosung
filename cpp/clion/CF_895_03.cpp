#include <iostream>
#include <cmath>
using namespace std;

int findD(int n) {
    if (n == 1) return -1;
    for (int d=2;d<=pow(n, 0.5);d++) {
        if (n % d == 0) return d;
    }
    return -1;
}

int main() {
    int T; cin >> T;
    while (T--) {
        int a, b; cin >> a >> b;
        if (b - a == 0) {
            int d = findD(a);
            if ( d == -1 ) cout << "-1\n";
            else cout << d << " " << d * (a / d -1) << "\n";
        }
        else {
            int x = b%2 == 0 ? b : b-1;
            if (x == 2) cout << "-1\n";
            else cout << 2 << " " << 2 * (x / 2 -1) << "\n";
        }
    }
}