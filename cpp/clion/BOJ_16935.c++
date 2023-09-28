#include <iostream>
using namespace std;
#define MAX 100

int board[MAX][MAX] = {0,};
int tmp[MAX][MAX] = {0,};
int R,C,M;

void tmpToBoard() {
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            board[r][c] = tmp[r][c];
        }
    }
}

void swap() {
    int t = R;
    R = C;
    C = t;
}

void op1() {
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            tmp[r][c] = board[R-1-r][c];
        }
    }
    tmpToBoard();
}

void op2() {
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            tmp[r][c] = board[r][C - 1 - c];
        }
    }
    tmpToBoard();
}

void op3() {
    swap();
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            tmp[r][c] = board[C-1-c][r];
        }
    }
    tmpToBoard();
}

void op4() {
    swap();
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            tmp[r][c] = board[c][R-1-r];
        }
    }
    tmpToBoard();
}

void op5() {
    int mr = R/2, mc = C/2;
    for (int r = 0; r < mr; r++) {
        for (int c = 0; c < mc; c++) {
            tmp[r][c] = board[r+mr][c];
        }
    }
    for (int r = 0; r < mr; r++) {
        for (int c = mc; c < C; c++) {
            tmp[r][c] = board[r][c - mc];
        }
    }
    for (int r = mr; r < R; r++) {
        for (int c = mc; c < C; c++) {
            tmp[r][c] = board[r - mr][c];
        }
    }
    for (int r = mr; r < R; r++) {
        for (int c = 0; c < mc; c++) {
            tmp[r][c] = board[r][c + mc];
        }
    }
    tmpToBoard();
}

void op6() {
    int mr = R/2, mc = C/2;
    for (int r = 0; r < mr; r++) {
        for (int c = 0; c < mc; c++) {
            tmp[r][c] = board[r][mc + c];
        }
    }
    for (int r = 0; r < mr; r++) {
        for (int c = mc; c < C; c++) {
            tmp[r][c] = board[r + mr][c];
        }
    }
    for (int r = mr; r < R; r++) {
        for (int c = mc; c < C; c++) {
            tmp[r][c] = board[r][c-mc];
        }
    }
    for (int r = mr; r < R; r++) {
        for (int c = 0; c < mc; c++) {
            tmp[r][c] = board[r-mr][c];
        }
    }
    tmpToBoard();
}

int main() {
    cin >> R >> C >> M;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            cin >> board[r][c];
        }
    }
    for (int i = 0; i < M; i++) {
        int op; cin >> op;
        if (op == 1) op1();
        else if (op == 2) op2();
        else if (op == 3) op3();
        else if (op == 4) op4();
        else if (op == 5) op5();
        else if (op == 6) op6();
    }
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            cout << board[r][c] << " ";
        }
        cout << "\n";
    }
}