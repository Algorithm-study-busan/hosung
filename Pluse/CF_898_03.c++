#include <iostream>
#include <string>
#include <vector>
using namespace std;

int score[10][10] = {
    {1,1,1,1,1,1,1,1,1,1},
    {1,2,2,2,2,2,2,2,2,1},
    {1,2,3,3,3,3,3,3,2,1},
    {1,2,3,4,4,4,4,3,2,1},
    {1,2,3,4,5,5,4,3,2,1},
    {1,2,3,4,5,5,4,3,2,1},
    {1,2,3,4,4,4,4,3,2,1},
    {1,2,3,3,3,3,3,3,2,1},
    {1,2,2,2,2,2,2,2,2,1},
    {1,1,1,1,1,1,1,1,1,1}
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int T; cin >> T;
    while (T--) {
        int ans = 0;
        vector<string> board;
        for (int r=0;r<10;r++) {
            string s; cin >> s;
            board.push_back(s);
        }

        for (int r=0;r<10;r++) {
            for (int c=0;c<10;c++) {
                ans += (board[r][c] == 'X' ? score[r][c] : 0);
            }
        }
        cout << ans << "\n";
    }
}