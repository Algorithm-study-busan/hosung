#include <iostream>
#include <string>
#include <vector>
using namespace std;

int R,C,sr,sc,er,ec,K;
string ans = "";
int dr[] = {1, 0, 0, -1};
int dc[] = {0, -1, 1, 0};
string m = "dlru";
string tmp = "";

bool inRange(int r, int c) {
    return r > 0 and r <= R and c > 0 and c <= C;
}

bool dfs(int r, int c) {
    if (tmp.size() == K) {
        if (r == er && c == ec) {
            ans = tmp;
            return true;
        }
        return false;
    }
    for (int i=0;i<4;i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (!inRange(nr,nc)) continue;
        tmp.push_back(m[i]);
        if (dfs(nr, nc)) return true;
        tmp.pop_back();
    }
    return false;
}

string solution(int n, int m, int x, int y, int r, int c, int k) {
    R = n; C = m; sr = x; sc = y; er = r; ec = c; K = k;
    if (dfs(sr, sc)) {
        return ans;
    }
    return "impossible";
}

int main() {
    cout << solution(3, 4, 2, 3, 3, 1, 5);
}