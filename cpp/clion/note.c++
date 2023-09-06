#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const pair<string, int> &a, pair<string, int> &b) {

    return a.second < b.second;
}

string solve(vector<pair<string, int> > &members) {
    while (!members.empty()) {
        int price = members.back().second;
        string name = members.back().first;
        int cnt = 0;
        while (!members.empty() && members.back().second == price) {
            members.pop_back();
            cnt += 1;
        }

        if (cnt == 1) {
            return name;
        }
    }
    return "NONE";
}

int main(void) {
    int n;
    cin >> n;

    vector<pair<string, int> > members;
    for (int i = 0; i < n; i++) {
        string name;
        int price;
        cin >> name >> price;

        pair<string, int> member;
        member.first = name;
        member.second = price;
        members.push_back(member);
    }

    sort(members.begin(), members.end(), compare);

    string result = solve(members);
    cout << result;

    return 0;
}