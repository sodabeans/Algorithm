// 길이 순서. 사전 순서.
// 중복 무시
#include <iostream>
#include <algorithm>

using namespace std;

void stringsort(string s[], int n){
    string key;
    int i, j = 0;
    
    for (i = 1; i < n; i++){
        key = s[i];
        for (j = i - 1; j >= 0 && s[j].length() > key.length(); j--){
            s[j + 1] = s[j];
        }
        s[j + 1] = key;
    }
    
}

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i, n = 0;
    cin >> n;
    
    string s[n];
    
    for (i = 0; i < n; i++){
        cin >> s[i];
    }
    
    sort(s, s+n);
    stringsort(s, n);
    
    cout << s[0] << "\n";
    for (i = 1; i < n; i++){
        if (s[i] != s[i - 1]){
            cout << s[i] << "\n";
        }
    }
    
    return 0;
}
