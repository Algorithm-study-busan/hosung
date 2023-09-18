#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int N; cin >> N;
    while(N--) {
        float a,b,c; cin >> a >> b >> c;
        cout << ceil((abs(a - b)/2)/c) << "\n";
    }
}