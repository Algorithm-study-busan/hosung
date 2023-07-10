#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Roket {
    int x,n;
    bool start;
    Roket(int x, bool start, int n) : x(x), start(start), n(n) {}
    bool operator< (const Roket &other) const {
        if (x == other.x) {
            return start < other.start;
        }
        return x < other.x;
    }
};

int solution(vector<vector<int>> targets) {
    vector<Roket> arr;
    vector<bool> distroied;
    vector<int> onTarget;
    distroied.resize(targets.size());
    for (int i = 0; i < onTarget.size(); i++) {
        onTarget[i] = false;
    }
    int ans = 0;

    for (int i=0;i<targets.size();i++) {
        arr.push_back(Roket(targets[i][0], true, i));
        arr.push_back(Roket(targets[i][1], false, i));
    }

    sort(arr.begin(), arr.end());

    for(Roket roket : arr) {
        if (distroied[roket.n]) continue;
        if (roket.start) {
            onTarget.push_back(roket.n);
        }
        else {
            ans += 1;
            while (!onTarget.empty()) {
                distroied[onTarget.back()] = true;
                onTarget.pop_back();
            }
        }
    }
    return ans;
}