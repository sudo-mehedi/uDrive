/*
ID: imehedi2
LANG: C++
TASK: friday
*/



#include <bits/stdc++.h>

using namespace std;

int dow(int d, int m, int y){
    int x = (d+=m<3 ? y-- : y-2,23*m/9+d+4+y/4-y/100+y/400) % 7;
    return x;
}


void solve(){
    int N;
    cin>>N;
    map<int, int>mp; 
    for(int i=0; i<7; i++) mp[i]= 0;
    int d = 13; 
    for(int y=1900; y<1900+N; y++){
        for(int m = 1; m<=12; m++){
            int x = dow(d, m, y);
            mp[x]++;
        }
    }
    cout << mp[6] << " " ;
    for(int i=0; i<6; i++){
        if(i==5) cout << mp[i] << endl;
        else
            cout << mp[i] << " "; 
    }
}

int main(){
    freopen("friday.in", "r", stdin);
    freopen("friday.out", "w", stdout);
    solve();
    return 0;
}
