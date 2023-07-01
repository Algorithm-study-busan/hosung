#include <iostream>
#include <queue>
#include <string>
#include <map>
using namespace std;
#define MAX 100001

struct Hard {
    int p,l;
    Hard(int p, int l) : p(p), l(l) {}

    bool operator<(const Hard &other) const {
        if (l == other.l) {
            return p < other.p;
        }
        return l < other.l;
    }
};

struct Easy {
    int p,l;
    Easy(int p, int l) : p(p), l(l) {}
    bool operator<(const Easy &other) const {
        if (l == other.l) {
            return p > other.p;
        }
        return l > other.l;
    }
};


int level[MAX] = {0,};
priority_queue<Hard> pqHard;
priority_queue<Easy> pqEasy;

void recommend(int x) {
    if (x == 1) {
        while(!pqHard.empty() && pqHard.top().l != level[pqHard.top().p]) {
            pqHard.pop();
        }
        cout << pqHard.top().p << "\n";
    }
    else {
        while(!pqEasy.empty() && pqEasy.top().l != level[pqEasy.top().p]) {
            pqEasy.pop();
        }
        cout << pqEasy.top().p << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int N; cin >> N;
    
    for (int i=0;i<N;i++) {
        int p,l; cin >> p >> l;
        pqHard.push(Hard(p,l));
        pqEasy.push(Easy(p,l));
        level[p] = l;
    }
    int M; cin >> M;
    for (int i=0;i<M;i++) {
        string s; cin >> s;
        if (s == "recommend") {
            int x; cin >> x;
            recommend(x);
        }
        else if (s == "add") {
            int p,l; cin >> p >> l;
            pqHard.push(Hard(p,l));
            pqEasy.push(Easy(p,l));
            level[p] = l;
        }
        else if (s == "solved") {
            int p; cin >> p;
            level[p] = 0;
        }
    }
}