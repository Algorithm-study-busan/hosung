#include <iostream>
#include <cstdlib>

using namespace std;
int N;
int *dist;
int x[4] = {0,}, y[4] = {0,};
void checkMap(int i){
    if (i%2==0) {
        dist[i] = y[1] - y[2];
    }
    else {
        dist[i] = x[1] - y[2];
    }
}

int main()
{
    cout << "________" << endl;
    cin >> N;
    dist =  new int[N];

    for(int i=0; i<N; i++) {
        if (i==0) {
            cin >> x[0] >> y[0];
            x[2] = x[0];
            y[2] = y[0];
            continue;
        }
        cin >> x[1] >> y[1];

        checkMap(i-1);
        x[2] = x[1];
        y[2] = y[1];
    }

    checkMap(N-1);

    int sum=0;
    for(int i=0;i<N;i++) {
        sum+= abs(dist[i]);
    }
    int time[5];
    for(int i=0; i<5; i++) {
        cin >>time[i];
    }
    for(int i=0;i<5;i++) {
        int res = time[i]%sum;
        int j=0;
        int x1 = x[0];
        int y1 = y[0];
        while(true) {
            if (res - abs(dist[j]) <0) break;
            res -= abs(dist[j]);
            j++;
        }
        for(int k=0;k<j;k++) {
            if (k%2==0) {
                y1 += dist[j];
            }
            else {
                x1 += dist[j];
            }
        }
        cout << x <<" "<< y<<endl;
    }
    delete dist;
}