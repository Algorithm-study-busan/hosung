#include <string>
#include <vector>

using namespace std;

vector<int> pre;

int binary_search(int l, int r) {
    int total = pre[r+1] - pre[l];
    if (total % 2 != 0) return 0;
    
    int fl = l;
    
    while (l<=r) {
        int mid = (l+r)/2;
        int tmp = pre[mid+1]-pre[fl];
        if (tmp == total/2) return total/2;
        else if(tmp < total/2) l = mid+1;
        else r = mid-1;
    }
    return 0;
}

int solution(vector<int> cookie) {
    pre.push_back(0);
    for (int c : cookie) {
        pre.push_back(pre.back() + c);
    }
    
    int ans = 0;
    for (int l = 0; l < cookie.size(); l++ ) {
        for (int r = l+1; r < cookie.size(); r++) {
            ans = max(ans, binary_search(l,r));
        }
    }
    return ans;
}