#include <iostream>
#include <set>
#include <vector>
#include <string>
using namespace std;
vector<string> board;
vector<string> strArr;
int R,C;

bool isOverlap(int cnt) {
    set<string> overlap;
    for (string &s : strArr) {
        s.pop_back();
        if (overlap.count(s) == 1) {
            return true;
        }
        overlap.insert(s); 
    }
    return false;
}

void solve() {
    for (int cnt = 0; cnt < R-1; cnt++) {
        if (isOverlap(cnt)) {
            cout << cnt;
            return;
        }
    }
    cout << R-1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> R >> C;
    for (int i=0;i<R;i++) {
        string s; cin >> s;
        board.push_back(s);
    }
    for (int c=0;c<C;c++) {
        string s;
        for (int r=R-1;r>=0;r--) {
            s.push_back(board[r][c]);
        }
        strArr.push_back(s);
    }
    solve();
}