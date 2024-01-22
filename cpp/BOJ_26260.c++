#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void search_front(const vector<int> &arr, int l, int r) {
    if (l == r) {
        cout << arr[l] << " ";
        return;
    }
    int mid = (l+r)/2;
    search_front(arr, l, mid-1);
    search_front(arr, mid+1, r);
    cout << arr[mid] << " ";
}

int main() {
    int N; cin >> N; 
    vector<int> arr;
    int x; 
    for (int i=0;i<N;i++) {
        cin >> x; 
        if (x != -1) arr.push_back(x);
    }
    cin >> x;
    arr.push_back(x);

    sort(arr.begin(), arr.end());
    search_front(arr, 0, N-1);
}