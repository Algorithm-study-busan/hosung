#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool canGo(vector<string> &board, char cc, map<char, pair<int,int>> &points1, map<char, pair<int,int>> &points2) {
    int sr = points1[cc].first;
    int sc = points1[cc].second;
    
    int er = points2[cc].first;
    int ec = points2[cc].second;
    
    if (sr == er) {
        for (int c=sc+1;c<ec;c++) {
            if (board[sr][c] != '.') return false;
        }
    } else if (sc == ec) {
        for (int r=sr+1;r<er;r++) {
            if (board[r][sc] != '.') return false;
        }
    } else {
        bool ck = false;
        if (sr < er && sc < ec) {
            for (int r=sr+1; r<er; r++) {
                if (board[r][sc] != '.') {
                    ck = true;
                    break;
                }
            }
            if (!ck) {
                for (int c=sc;c<ec;c++) {
                    if (board[er][c] != '.') {
                        ck = true;
                        break;
                    }
                }
            }
            
            if (ck) {
                for (int c=sc+1; c<ec;c++) {
                    if (board[sr][c] != '.') return false;
                }
                for (int r=sr;r<er;r++) {
                    if (board[r][ec] != '.') return false;
                }
            }
        } else {
            bool ck = false;
            for (int r=sr+1;r<er;r++) {
                if (board[r][sc] != '.') {
                    ck = true;
                    break;
                }
            }
            if (!ck) {
                for (int c=ec+1;c<sc+1;c++) {
                    if (board[er][c] != '.') {
                        ck = true;
                        break;
                    }
                }
            }
            
            if (ck) {
                for (int c=ec;c<sc;c++) {
                    if (board[sr][c] != '.') return false;
                }
                for (int r=sr;r<er;r++) {
                    if (board[r][ec] != '.') return false;
                }
            }
        }
    }
    
    
    board[sr][sc] = '.';
    board[er][ec] = '.';
    return true;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
string solution(int m, int n, vector<string> board) {
    map<char, pair<int,int>> points1, points2;
    vector<char> arr;
    for (int r=0;r<m;r++) {
        for (int c=0;c<n;c++) {
            if (board[r][c] == '.' || board[r][c] == '*') continue;
            if (points1.count(board[r][c])) {
                points2.insert({board[r][c], {r,c}});
            }
            else {
                points1.insert({board[r][c], {r,c}});
                arr.push_back(board[r][c]);
            }
        }
    }
    sort(arr.begin(), arr.end());
    
    bool selected[30] = {0,};
    string ans = "";
    
    while (ans.size() < arr.size()) {
        bool ck = false;
        for (char c : arr) {
            if (selected[c-'A']) continue;
            
            if (canGo(board, c, points1, points2)) {
                selected[c-'A'] = true;
                ans += c;
                ck = true;
                break;
            }
        }
        if (!ck) return "IMPOSSIBLE";
    }
    
    return ans;
}