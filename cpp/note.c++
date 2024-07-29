#include <iostream>
#include <vector>
using namespace std;

int N, k;
vector<int> items;

struct customer {
    int id;
    int item;
};



int ch_min() {
    int ch;
    int m = items[0];
    for(int i=1;i<k;i++) {
        if(m>items[i]) {
            ch = i;
            m = items[i];
        }
    }
    return ch;
}

int dp[100] = {0,};

int fibo(int x) {
    if (dp[x] != 0) return dp[x];
    if (x == 0 || x == 1) return 1;
    dp[x] = fibo(x-1) + fibo(x-2);
    return dp[x];
}

int main() {
    fibo(5);
}