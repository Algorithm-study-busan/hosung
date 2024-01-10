#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    int ret = 0;
    for (int i=0;i<N;i++) {
        int x; cin >> x;
        ret ^= x;
    }

    cout << (ret != 0 ? "koosaga" : "cubelover");
}