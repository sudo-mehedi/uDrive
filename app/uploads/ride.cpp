/*
ID: imehdi2;
LANG: C++
TASK: ride
*/
#include <bits/stdc++.h>

using namespace std;

void solve(){
    string s1;
    string s2;
    cin>>s1>>s2; 
    int64_t n1 = 1;
    int64_t  n2 = 1;

    for(unsigned int i=0; i<s1.size(); i++){
        n1*= ((int)s1[i] - 64) ;
    }

    for(unsigned int i=0; i<s2.size(); i++){
        n2*= ((int)s2[i] - 64);
    }

    if(n1%47 == n2%47) {
        cout << "GO" << endl;
    }else{
        cout << "STAY" << endl;
    }

}

int main(){
    freopen("ride.in", "r", stdin); 
    freopen("ride.out", "w", stdout);
    solve();
    return 0;
}
