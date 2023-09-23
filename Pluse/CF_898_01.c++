#include <iostream>
#include <string>
using namespace std;

string swap(string s, int a, int b) {
    char tmp = s[a];
    s[a] = s[b];
    s[b] = tmp;
    return s;
}

int main() {
    int T; cin >> T;
    while (T--) {
        string s; cin >> s;
        if (s == "abc" || swap(s,0,1) == "abc" || swap(s,0,2) == "abc" || swap(s, 1,2) == "abc") {
            cout << "YES\n";
        }
        else {
            cout << "NO\n";
        }
    }
}