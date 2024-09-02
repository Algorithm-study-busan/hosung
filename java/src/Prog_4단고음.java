// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int ans, k;

void dfs(int n, int mcnt, int pcnt) {
    if (n == 1) {
        if (mcnt == k && pcnt == 2*k) ans++;
        return;
    }
    if (mcnt > k || pcnt > 2*k || mcnt*2 > pcnt) {
        return;
    }
    if (n % 3 == 0) dfs(n/3, mcnt+1, pcnt);
    dfs(n-1, mcnt, pcnt+1);
}

int solution(int n) {
    ans = 0;
    k = 0;
    long tmp = 1;
    while(tmp < n) {
        tmp *= 3;
        k++;
    }
    k--;
    
    dfs(n, 0,0);
    return ans;
}