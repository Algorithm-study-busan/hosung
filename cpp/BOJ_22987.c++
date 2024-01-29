#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    double arr[100000] = {0,};
    double ans = 0;
    for (int i=0;i<N;i++) {
        cin >> arr[i];
    }
    if (N==1) {
        cout << arr[0];
        return 0;
    }
    
    ans += arr[0]*2;
    ans += arr[N-1]*2;

    for (int i=1;i<N-1;i++) {
        ans += arr[i]*3;
        ans -= (arr[i]*arr[i-1])*2;
    }
    ans -= (arr[N-1] * arr[N-2])*2;
    
    cout << ans;
}