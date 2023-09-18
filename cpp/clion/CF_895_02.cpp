#include <iostream>
#include <cstring>
using namespace std;

int s[401] = {0,};

int main() {
    int T; cin >> T;
    while (T--) {
        memset(s, 0, sizeof(s));
        int N; cin >> N;
        while (N--) {
            int a,b; cin >> a >> b;
            if (s[a] == 0) s[a] = b;
            else s[a] = min(s[a], b);
        }
        int maxLen = 987654321;
        for (int i = 1; i <= 400; i++) {
            maxLen--;
            if (s[i] != 0) {
                maxLen = min(maxLen, (s[i] -1) / 2);
            }
            if (maxLen == 0) {
                cout << i << '\n';
                break;
            }
        }
    }
}