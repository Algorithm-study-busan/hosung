#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Node {
    int a, b, n;
    Node (int a, int b, int n) : a(a), b(b), n(n) {}

    bool operator<(const Node &o) const {
        if (a == o.a) return b > o.b;
        return a < o.a;
    }
};

int main() {
    int N; cin >> N;
    int M; cin >> M;

    vector<Node> arr1;
    vector<Node> arr2;

    for (int i=1;i<=M;i++) {
        int a,b; cin >> a >> b;
        if (a > b) {
            arr1.push_back(Node(a-N, b, i));
            arr2.push_back(Node(a, b+N, i));
        } else {
            arr1.push_back(Node(a,b,i));
            arr2.push_back(Node(a,b,i));
        }
    }

    sort(arr1.begin(), arr1.end());
    sort(arr2.begin(), arr2.end());

    vector<bool> ans(M+1, true);

    int last_b = -N;
    for (Node node : arr1) {
        if (node.b <= last_b) {
            ans[node.n] = false;
        } else {
            last_b = node.b;
        }
    }

    last_b = -N;
    for (Node node : arr2) {
        if (node.b <= last_b) {
            ans[node.n] = false;
        } else {
            last_b = node.b;
        }
    }

    for (int n=1;n<=M;n++) {
        if (ans[n]) cout << n << " ";
    }
}