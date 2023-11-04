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
    int ch = 0;
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
    cin >>N>>k;
    vector<customer> c_list;
    vector<vector<customer> > channel;
    for(int i=0;i<N;i++) {
        customer c;
        cin >> c.id >> c.item;
        c_list.push_back(c);
    }

    for(int i = 0;i<k;i++) {
        vector<customer> a;
        channel.push_back(a);
        items.push_back(0);
    }

    for(int i=0;i<N;i++) {
        int ch = ch_min();
        cout << ch << endl;
        items[ch] += c_list[i].item;
        channel[ch].push_back(c_list[i]);
    }

    int res = 0;
    while(res < N) {
        for(int i=k-1;i>=0;i--) {
            channel[i][0].item--;
            if(channel[i][0].item == 0) {
                cout << channel[i][0].id << endl;
                channel[i].erase(channel[i].begin());
                res++;
            }
        }
    }
}