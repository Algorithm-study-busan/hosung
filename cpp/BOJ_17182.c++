#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std; 
#define MAX 10
#define INF 987654321
int edge[MAX][MAX] = {0,};
int N, S;

int main() {
    cin >> N >> S;
    for (int i=0;i<N;i++) {
        for (int j=0;j<N;j++) {
            cin >> edge[i][j];
        }
    }

    for (int a=0;a<N;a++) {
        for (int b=0;b<N;b++) {
            if (a == b) continue;
            for (int c=0;c<N;c++) {
                if (a == c || b == c) continue;
                    edge[a][c] = min(edge[a][c], edge[a][b] + edge[b][c]);
            }
        }
    }
    vector<int> arr;
    for (int i=0;i<N;i++) {
        if (i == S) continue;
        arr.push_back(i);
    }

    int ans = INF;
    do {
        int last = S;
        int tmp = 0;
        for (int n : arr) {
            tmp += edge[last][n];
            last = n;
        }
        ans = min(ans, tmp);
    } while(next_permutation(arr.begin(), arr.end()));
    cout << ans;
}