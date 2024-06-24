/*
ID: imehedi2
LANG: C++
TASK: beads
*/

#include <bits/stdc++.h>

using namespace std;
//using uit = unsigned int;
void solve(){
    int n;
    cin>>n;
    string s;
    cin>>s;
    s+=s;
    int mx = 0;    
    for(int i=0; i<2*n; i++){
        int cnt = 0;
        char state = s[i];
        int k = i;
        if(s[i] != 'w') {
            for(int j=0; j<2; j++){
                while( (s[k]==state or s[k] == 'w') and k<2*n){
                    cnt++;
                    k++;
                }
                state = s[k];
            }
        }else{
            for(int j=0; j<3; j++){
                while( (s[k]==state or s[k] == 'w') and k<2*n){
                    cnt++;
                    k++;
                }
                state = s[k];
            }

        }
        mx = max(cnt, mx);
    }
    if(mx>n)
        cout << n << endl;
    else
        cout << mx << endl;

}

int main(){
    freopen("beads.in", "r", stdin);
    freopen("beads.out", "w", stdout);
    solve();
    return 0;
}

