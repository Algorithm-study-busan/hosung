#include <iostream>
#include <string>
using namespace std;

void swap(string &a, string &b) {
    string tmp = a;
    a = b;
    b = tmp;
}

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    if (s1.size() < s2.size()) swap(s1, s2);
    int totalLength = s1.size() + s2.size();
    int ans = totalLength;

    for (int i=0;i<s2.size();i++) {
        bool ck = true;
        for (int j=0;j<=i;j++) {
            if (s1[j] == '2' && s2[s2.size()-1-i+j] == '2') {
                ck = false;
                break;
            }
        }
        if (ck) ans = min(ans, totalLength -i -1);
    }

    for (int i=0;i<=s1.size()-s2.size();i++) {
        bool ck = true;
        for (int j=0;j<=s2.size();j++) {
            if (s2[j] == '2' && s1[i+j] == '2') {
                ck = false;
                break;
            }
        }
        if (ck) ans = min(ans, (int)s1.size());
    }

    for (int i=0;i<s2.size();i++) {
        bool ck = true;
        for (int j=0;j<=i;j++) {
            if (s2[j] == '2' && s1[s1.size()-1-i+j] == '2') {
                ck = false;
                break;
            }
        }
        if (ck) ans = min(ans, totalLength -i -1);
    }
    cout << ans;
}