#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N; cin >> N;
    vector<pair<int,int>> arr;
    for (int i=0;i<N;i++) {
        int s,e; cin >> s >> e;
        arr.push_back({s,1});
        arr.push_back({e,-1});
    }
    
    sort(arr.begin(), arr.end());

    int floor = 0;
    int ans = 0;
    for (auto p : arr) {
        floor += p.second;
        ans = max(ans, floor); 
    }

    cout << ans;
}