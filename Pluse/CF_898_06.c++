#include <iostream>
#include <string>
using namespace std;

int countLeft(const string &s, int idx) {
    int ret = 0;
    while (idx >= 0) {
        if (s[idx] == 'A') {
            ret++;
            idx--;
        } else {
            return ret;
        }
    }
    return ret;
}

int countRight(const string &s, int idx) {
    int ret = 0;
    while (idx < s.size()) {
        if (s[idx] == 'A') {
            ret++;
            idx++;
        } else {
            return ret;
        }
    }
    return ret;
}

int checkRight(const string &s, int idx) {
    for (int i=idx;i<s.size();i++) {
        if (s[i] == 'B') return false;
    }
    return true;
}

int main() {
    int T; cin >> T;
    while (T--) {
        string s; cin >> s;
        int ans = 0;
        for (int i=0;i<s.size();i++) {
            if (s[i] == 'B') {
                int leftCount = countLeft(s, i-1);
                int rightCount = countRight(s, i+1);
                if (checkRight(s, i+1) && leftCount < rightCount) {
                    ans += rightCount;
                    break;
                }
                ans += leftCount; 
            }
        }
        cout << ans << "\n";
    }
}