#include <iostream>
#include <stack>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    
    int N; cin >> N;
    stack<int> stk;

    int ans = 0;
    for(int i=0;i<N;i++) {
        int x,y; cin >> x >> y;

        while(!stk.empty() && stk.top() > y) {
            stk.pop();
        }

        if (stk.empty() || stk.top() != y) {
            if (y == 0) continue;
            ans++;
            stk.push(y);
        }
    }
    cout << ans;
}