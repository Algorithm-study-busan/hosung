#include <vector>
#include <map>
#include <algorithm>
using namespace std;

bool cmp(vector<int> &o1, vector<int> &o2) {
    return o1[1] < o2[1];
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<vector<int>> data) {
    unordered_map<int,int> xMap,yMap;
    sort(data.begin(), data.end(), cmp);
    
    int idx = 1;
    for (auto point : data) {
        if (yMap.count(point[1]) == 0) {
            yMap.insert({point[1], idx++});
        }
    }
    
    sort(data.begin(), data.end());
    idx = 1;
    for (auto point : data) {
        if (xMap.count(point[0]) == 0) {
            xMap.insert({point[0], idx++});
        }
    }
    
    int dp[5001][5001] = {0,};
    for (auto point : data) {
        int x = xMap[point[0]];
        int y = yMap[point[1]];
        
        dp[x][y]++; 
    }
    
    for (int x=1;x<=5000;x++) {
        for (int y=1;y<=5000;y++) {
            dp[x][y] += dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1];
        }
    }
    
    int ans = 0;
    for (int i=0;i<data.size();i++){
        for (int j=i+1;j<data.size();j++) {
            int x1 = xMap[data[i][0]];
            int y1 = yMap[data[i][1]];
            int x2 = xMap[data[j][0]];
            int y2 = yMap[data[j][1]];
            
            if (x1 == x2 || y1 == y2) continue;
            
            int cnt = dp[max(x1,x2)-1][max(y1,y2)-1] - dp[min(x1,x2)][max(y1,y2)-1] - dp[max(x1,x2)-1][min(y1,y2)] + dp[min(x1,x2)][min(y1,y2)];
            
            if (cnt == 0) ans ++;
        }
    }
    
    return ans;
}