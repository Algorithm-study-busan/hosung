#include <iostream>
#include <vector>
using namespace std;
#define ll long long

bool check(const vector<int> &arr, int h, int x) {
    ll water = 0;
    for (int w : arr) {
        water += max(h-w, 0);
    }
    return water <= x;
}

int binarySearch(const vector<int> &arr, int x) {
    int lo = 0;
    ll hi = 2000000001;
    while (lo <= hi) {
        ll mid = (lo+hi)/2;
        if (check(arr, mid, x)) lo = mid+1;
        else hi = mid-1;
    }
    return lo;
}



int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int T; cin >> T;
    vector<int> arr;
    while (T--) {
        int n, x; cin >> n >> x;
        arr.clear();
        for (int i=0;i<n;i++) {
            int w; cin >> w;
            arr.push_back(w);
        }
        cout << binarySearch(arr, x)-1 << "\n";
    }
}