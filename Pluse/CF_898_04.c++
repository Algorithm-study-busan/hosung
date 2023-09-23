#include <iostream>
#include <string>
using namespace std;

int main() {
    int T; cin >> T;
    while(T--) {
        int n,k; cin >> n >> k;
        string s; cin >> s;
        int ans = 0;
        for (int i=0;i<n;i++) {
            if (s[i] == 'B') {
                ans++;
                i += k-1;
            }
        }
        cout << ans << "\n";
    }
}