#include <iostream>
#include <vector>
#include <string>
using namespace std;

int dr[] = {-1,0,1,0};
int dc[] = {0,1,0,-1};

void move(vector<string> &board, int &cr, int &cc, int k) {
    int nr = cr + dr[k];
    int nc = cc + dc[k];
    if (board[nr][nc] == '.') {
        cr = nr;
        cc = nc;
    }
    else if (board[nr][nc] == '#') return;
    else if (board[nr][nc] == 'b') {
        int nnr = cr + dr[k]*2;
        int nnc = cc + dc[k]*2;

        if (board[nnr][nnc] == '.') {
            cr = nr;
            cc = nc;
            board[nr][nc] = '.';
            board[nnr][nnc] = 'b';
        }
        else if (board[nr][nc] == '#') return;
    }
}

bool complete(const vector<string> &board, int R, int C, bool ends[15][15]) {
    for (int r=0;r<R;r++) {
        for (int c=0;c<C;c++) {
            if (ends[r][c] && board[r][c] != 'b') return false;
        }
    }
    return true;
}

int main() {
    int game = 1;
    while(1) {
        int R,C; cin >> R >> C;
        if (R == 0 && C == 0) break;
        vector<string> board;
        for (int i=0;i<R;i++) {
            string s; cin >> s;
            board.push_back(s);
        }

        int sr=-1;
        int sc=-1;

        bool ends[15][15] = {0,};

        for (int r=0;r<R;r++) {
            for (int c=0;c<C;c++) {
                if (board[r][c] == 'w') {
                    board[r][c] = '.';
                    sr=r;
                    sc=c;
                }
                else if (board[r][c] == '+') {
                    board[r][c] = '.';
                    ends[r][c] = true;
                }
                else if (board[r][c] == 'W') {
                    board[r][c] = '.';
                    sr=r;
                    sc=c;
                    ends[r][c] = true;
                }
                else if (board[r][c] == 'B') {
                    board[r][c] = 'b';
                    ends[r][c] = true; 
                }
            }
        }

        string ops; cin >> ops;

        bool res = false;
        for (char op : ops) {
            int k = -1;
            if (op == 'U') k = 0;
            else if (op == 'R') k = 1;
            else if (op == 'D') k = 2; 
            else k = 3;

            move(board, sr, sc, k);
            if (complete(board, R, C, ends)) {
                res = true;
                break;
            }
        }


        for (int r=0;r<R;r++) {
            for (int c=0;c<C;c++) {
                if (ends[r][c]) {
                    if (board[r][c] == 'b') {
                        board[r][c] = 'B';
                    } else {
                        board[r][c] = '+';
                    }
                } 
            }
        }

        if (ends[sr][sc]) {
            board[sr][sc] = 'W';
        } else {
            board[sr][sc] = 'w';
        }

        cout << "Game " << game;
        cout << (res ? ": complete\n" : ": incomplete\n");
        for (string s : board) {
            cout << s << "\n";
        }
        game++;
    }
}