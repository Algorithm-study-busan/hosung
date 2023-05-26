#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
int X, Y, ex, ey;
map<pair<int,int>, int> visited;

pair<int,int> FL(pair<int,int> bottles) {
    bottles.first = X;
    return bottles;
}

pair<int,int> FR(pair<int,int> bottles) {
    bottles.second = Y;
    return bottles;
}

pair<int,int> EL(pair<int,int> bottles) {
    bottles.first = 0;
    return bottles;
}

pair<int,int> ER(pair<int,int> bottles) {
    bottles.second = 0;
    return bottles;
}

pair<int,int> MR(pair<int,int> bottles) {
    int pour = min(Y - bottles.second, bottles.first);
    bottles.second += pour;
    bottles.first -= pour;
    return bottles;
}

pair<int,int> ML(pair<int,int> bottles) {
    int pour = min(X - bottles.first, bottles.second);
    bottles.first += pour;
    bottles.second -= pour;
    return bottles;
}

pair<int,int> (*arr[])(pair<int,int>) = {FL,FR,EL,ER,ML,MR};

void bfs() {
    visited[{0,0}] = 1;
    queue<pair<int,int>> q;
    q.push({0,0});
    while(!q.empty()) {
        pair<int,int> cur = q.front();
        q.pop();

        if (cur.first == ex && cur.second == ey) {
            cout << visited[cur]-1;
            return;
        }

        for (auto f : arr) {
            pair<int,int> nxt = f(cur);
            if (visited[nxt] > 0) continue;
            visited[nxt] = visited[cur]+1;
            q.push(nxt);
        }
    }
    cout << -1;
}

int main() {
    cin >> X >> Y >> ex >> ey;
    bfs();
}