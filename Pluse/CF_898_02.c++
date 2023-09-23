#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int T; cin >> T;
    while (T--) {
        int N; cin >> N;
        vector<int> arr;
        for (int i=0;i<N;i++) {
            int x; cin >> x;
            arr.push_back(x);
        }
        int ans = 1;
        sort(arr.begin(), arr.end());
        ans *= arr[0]+1;
        for (int i=1;i<N;i++) {
            ans *= arr[i];
        }
        cout << ans << "\n";
    }
}