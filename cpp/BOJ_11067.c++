#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 100001

struct Point {
    int x,y;
    Point(int x, int y) : x(x), y(y) {}

    bool operator<(const Point &other) const {
        if (x == other.x) {
            return y < other.y;
        }
        return x < other.x;
    }
};

int main() {
    int T; cin >> T;
    while(T--) {
        int N; cin >> N;
        int cnt[MAX] = {0,};

        vector<Point> arr;
        for (int i=0;i<N;i++) {
            int x,y; cin >> x >> y;
            cnt[x]++;
            arr.push_back(Point(x,y));
        }

        sort(arr.begin(), arr.end());

        vector<Point> ans;
        ans.push_back(Point(-1,0));

        for (int i=0;i<N;i++) {
            if (arr[i].x != ans.back().x && arr[i].y != ans.back().y) {
                for (int k=cnt[arr[i].x]-1;k>=0;k--) {
                    ans.push_back(arr[i + k]);
                }
                i += cnt[arr[i].x]-1;
            }
            else {
                ans.push_back(arr[i]);
            }
        }

        int M; cin >> M;
        for (int i=0;i<M;i++) {
            int idx; cin >> idx;
            cout << ans[idx].x << " " << ans[idx].y << "\n";
        }
    }
}