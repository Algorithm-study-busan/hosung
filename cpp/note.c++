#include <iostream>
#include <vector>
#include <map>
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

int main() {
    map<char, pair<int,int>> m;
    m.insert({'a', {1,2}});
    
    cout << m['a'].first << " " << m['a'].second << endl;
    vector<int> arr;
    arr.
}