#include <iostream>
#include <string>

using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    string s;
    
    while (1){
        bool palindrome = true;
        cin >> s;
        
        if (s == "0"){
            break;
        }
        
        for (int i = 0; i < s.length() / 2; i++){
            if (s[i] != s[s.length() - 1 - i]){
                palindrome = false;
                break;
            }
        }
        
        if (palindrome){
            cout << "yes\n";
        } else {
            cout << "no\n";
        }
        
    }
    
    return 0;
}
