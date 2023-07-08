#include <iostream>
using namespace std;
#define MAX 1000001
int parent[MAX] = {0,};
int cnt[MAX] = {0,};

int getParent(int a) {
    if (a == parent[a]) return a;
    return parent[a] = getParent(parent[a]);
}

bool isSet(int a, int b) {
    a = getParent(a);
    b = getParent(b);

    return a == b;
}

void unionNode(int a, int b) {
    a = getParent(a);
    b = getParent(b);

    if (a < b) {
        parent[b] = a;
        cnt[a] += cnt[b];
    }
    else {
        parent[a] = b;
        cnt[b] += cnt[a];
    }
}

int main() {
    int N; cin >> N;
    for (int i=0;i<MAX;i++) {
        parent[i] = i;
        cnt[i] = 1;
    }

    for (int i=0;i<N;i++) {
        char op; cin >> op;

        if (op == 'I') {
            int a,b; cin >> a >> b;
            if (isSet(a, b)) {
                continue;
            }
            else {
                unionNode(a, b);
            }
        }
        else {
            int a; cin >> a;
            cout << cnt[getParent(a)] << "\n";
        }
    }
}