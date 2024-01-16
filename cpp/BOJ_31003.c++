#include <iostream>
#include <queue>
#include <vector>
using namespace std;
vector<int> edges[3000];
int inDegree[3000] = {0,};
int arr[3000] = {0,};

struct Node {
    int idx, num;
    Node(int idx, int num) : idx(idx), num(num) {}

    bool operator<(const Node &other) const {
        return num > other.num;
    }
};

bool isCoPrime(int a, int b) {
    int c = a % b;
    while (b != 0) {
        c = a % b;
        a = b;
        b = c;
    }
    return a == 1;
}



int main() {
    int N; cin >> N;
    for (int i=0;i<N;i++) cin >> arr[i];

    for (int i=0;i<N;i++) {
        for (int j=i+1;j<N;j++) {
            if (!isCoPrime(arr[i], arr[j])) {
                edges[i].push_back(j);
                inDegree[j]++;
            }
        }
    }
    
    priority_queue<Node> pq;
    for (int i=0;i<N;i++) {
        if (inDegree[i] == 0) pq.push(Node(i, arr[i]));
    }

    while (!pq.empty()) {
        Node cur = pq.top();
        pq.pop();
        cout << cur.num << " ";

        for (int next : edges[cur.idx]) {
            if (--inDegree[next] == 0) {
                pq.push(Node(next, arr[next]));
            } 
        }
    }
}