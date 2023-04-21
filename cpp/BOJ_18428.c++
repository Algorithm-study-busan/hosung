#include <iostream>
#include <vector>
using namespace std; 
int N;

char board[6][6];
vector<pair<int,int>> teachers;
int dr[] = {-1,0,1,0};
int dc[] = {0,-1,0,1};

bool ans = false;

bool inRange(int r, int c) {
    return (r>=0 && r<N && c>=0 && c<N);
}

bool solve() {
    for (auto p : teachers) {
        int r = p.first;
        int c = p.second;

        for (int d=0;d<4;d++) {
            for (int k=1;k<6;k++) {
                int nr = r + dr[d]*k;
                int nc = c + dc[d]*k;
                if (!inRange(nr,nc) || board[nr][nc] == 'O') break;
                if (board[nr][nc] == 'S') return false;
            }
        }
    }
    return true;
}

void brute(int idx, int cnt) {
    if (cnt == 3) {
        ans = ans || solve();
        return;
    }
    if (idx == N*N) return;
    int r = idx/N;
    int c = idx%N;


    brute(idx+1, cnt);
    if (board[r][c] == 'X') {
        board[r][c] = 'O';
        brute(idx+1, cnt+1);
        board[r][c] = 'X';
    }
}

int main() {
    cin >> N;
    for (int r=0;r<N;r++) {
        for (int c=0;c<N;c++) {
            cin >> board[r][c];
            if (board[r][c] == 'T') {
                teachers.push_back({r,c});
            }
        }
    }
    brute(0,0);

    cout << (ans == true ? "YES" : "NO");
}