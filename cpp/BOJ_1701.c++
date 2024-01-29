#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std; 

vector<int> findPi(string s) {
    int j = 0;
    vector<int> ret(s.size(), 0);
    for (int i=1;i<s.size();i++) {
        while (j > 0 && s[i] != s[j]) {
            j = ret[j-1];
        }
        if (s[i] == s[j]) ret[i] = ++j;
    }
    return ret;
}

int main() {
    string s; cin >> s;
    int ans = -1;
    for (int i=0;i<s.size();i++) {
        string subStr = s.substr(i,s.size());
        vector<int> pi = findPi(subStr);
        int tmp = *max_element(pi.begin(), pi.end());
        ans = max(ans, *max_element(pi.begin(), pi.end()));
    }
    cout << ans;
}