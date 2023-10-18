#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr;
    arr.resize(3);
    cout << arr.capacity() << endl;
    arr.push_back(1);
    cout << arr.capacity();
}