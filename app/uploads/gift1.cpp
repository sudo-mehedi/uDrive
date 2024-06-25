/*
ID: imehedi2
LANG: C++
TASK: gift1
*/

#include <bits/stdc++.h>

using namespace std;

void solve(){
    int n;
    cin>>n;
    
    unordered_map<string, int> ump;
    vector<string>ss;
    for(int i=0; i<n; i++){
        string tmp;
        cin>>tmp;
        ump[tmp] = 0;
        ss.push_back(tmp);
    }

    for(int i=0; i<n; i++){
        string doner;
        cin>>doner;
        int w_amnt,r_num;
        
        cin>>w_amnt>>r_num;
        if(r_num == 0) continue; 
        ump[doner]-=w_amnt;
        ump[doner] += (w_amnt%r_num);
        w_amnt = w_amnt - w_amnt%r_num;
        for(int j=0; j<r_num; j++){
            string s;
            cin>>s;
            ump[s]+= w_amnt/r_num;
        }

    }
    
    for(auto it: ss){
        cout << it << " " << ump[it] << endl;
    }
    
}


int main(){
    freopen("gift1.in", "r", stdin);
    freopen("gift1.out", "w", stdout);
    solve();
    return 0;
}
