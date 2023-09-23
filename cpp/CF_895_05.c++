#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define ll long long

int main() {
    int T; cin >> T;
    while (T--) {
        int N; cin >> N;
        int arr[100000] = {0,};
        ll x = 0, y = 0;
        for (int i=0;i<N;i++) {
            cin >> arr[i];
        }
        string s; cin >> s;
        for (int i=0;i<N;i++) {
            if (s[i] == '0') x ^= arr[i];
            else y ^= arr[i];
        }

        ll totalXor = 0;
        ll reculXor[100001] = {0,};
        for (int i=1;i<=N;i++) {
            totalXor ^= arr[i-1];
            reculXor[i] = totalXor;
        }
        
        int Q; cin >> Q;
        vector<ll> ans;
        for (int i=0;i<Q;i++) {
            int op; cin >> op;
            if (op == 2) {
                int k = 0; cin >> k;
                if (k == 0) {
                    ans.push_back(x);
                }
                else {
                    ans.push_back(y);
                }
            }
            else {
                int a,b; cin >> a >> b;
                x ^= reculXor[b] ^ reculXor[a-1];
                y ^= reculXor[b] ^ reculXor[a-1];
            }
        }

        for(int x : ans) {
            cout << x << " ";
        }
        cout << "\n";
    }
}