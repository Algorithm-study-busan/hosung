#include <iostream>
#include <vector>
#include <set>
using namespace std;
#define MAX 1001
int SET[MAX] = {0,};

struct Rec {
    int x1,y1, x2, y2;
    Rec(int x1, int y1, int x2, int y2) : x1(x1), y1(y1), x2(x2), y2(y2) { }
};

bool outOfRec(const Rec &A, const Rec &B) {
    return A.y2 < B.y1 || A.y1 > B.y2 ||
        B.x1 > A.x2 || B.x2 < A.x1;
}

bool BinA(const Rec &A, const Rec &B) {
    return A.x1 < B.x1 && B.x2 < A.x2 && 
            A.y1 < B.y1 && B.y2 < A.y2;
}

int getParent(int a) {
    if (a == SET[a]) return a;
    return SET[a] = getParent(SET[a]);
}

void unionNode(int a, int b) {
    a = getParent(a);
    b = getParent(b);

    if (a < b) SET[b] = a;
    else SET[a] = b;
}

int main() {
    vector<Rec> arr;
    int N; cin >> N;
    arr.push_back(Rec(0,0,0,0));
    for (int i=0;i<=N;i++) SET[i] = i;
    for (int i=0;i<N;i++) {
        int x1,y1, x2,y2; cin >> x1 >> y1 >> x2 >> y2;
        arr.push_back(Rec(x1,y1, x2,y2));
    }

    for (int i=0;i<=N;i++) {
        for (int j=i+1;j<=N;j++) {
            Rec A = arr[i];
            Rec B = arr[j];
            if (outOfRec(A,B) || BinA(A,B) || BinA(B,A)) continue;
            unionNode(i,j);
        }
    }

    set<int> s;
    for (int i=1;i<=N;i++) {
        int n = getParent(i);
        if (n != 0) s.insert(n);
    }
    cout << s.size();
}