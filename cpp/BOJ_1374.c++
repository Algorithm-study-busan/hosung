#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<pair<int,int>> arr;
    int N; cin >> N;
    for (int i=0;i<N;i++) {
        int n, s, e; cin >> n >> s >> e;
        arr.push_back({s,1});
        arr.push_back({e,-1});
    }
    sort(arr.begin(), arr.end());
    int ans = 0;
    int tmp = 0;

    for (auto p : arr) { 
        tmp += p.second;
        ans = max(ans, tmp);
    }
    cout << ans;
}