#include <iostream>
using namespace std;
int ans = 987654321;

void find_ans(int x1, int y1, int x2, int y2, int x, int y, int K) {
    if (K==0) return;
    if ((x1 <= x && x < x2) && (y1 <= y && y < y2)) {
        ans = min(ans, K);

        int dx = x2 - x1;
        int dy = y2 - y1;

        if (dx < dy) {
            find_ans(x1, y1, x1 + dx, y1 + (dy-dx), x, y, K-1);
            find_ans(x2 - dx, y2 - (dy-dx), x2, y2 , x, y, K-1);
        }
        else {
            find_ans(x1, y1, x1 + (dx-dy), y1 + dy, x, y, K-1);
            find_ans(x2 - (dx-dy), y2 - dy, x2, y2, x, y, K-1);
        }
    }
}

int main() {
    int x2, y2; cin >> x2 >> y2;
    int x,y; cin >> x >> y;

    int n1 = 1;
    int n2 = 1;
    int N = 1;
    int tmp = -1;
    for (int n=1;n<=1000;n++) {
        if ((n1 == x2 && n2 == y2) || (n1 == y2 && n2 == x2)) {
            N = n;
            break;
        }
        tmp = n2;
        n2 = n1 + n2;
        n1 = tmp;
    }
    find_ans(0,0,x2,y2, x,y, N);
    cout << ans;
}