//tried with string. did not work. gonna try with array next.
#include <iostream>
#include <string>

using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    string str;
    string in;
    string opr;
    int i, n, m = 0;
    
    cin >> str;
    n = str.length();
    cin >> m;
    
    for (i = 0; i < m; i++){
        cin >> opr;
        if (opr == "L"){
            if (n > 0){
                n--;
            }
        } else if (opr == "D"){
            if (n != str.length()){
                n++;
            }
        } else if (opr == "B"){
            // problem here
            if (n > 1 && n == str.length()){
                str.erase(n - 1);
                n = str.length();
            } else if (n > 1 && n != str.length()){
                str.erase(n - 1);
                n--;
            } else if (n == 1){
                str.erase(0);
            }
        } else {
            cin >> in;
            str.insert(n, in);
        }
        cout << str << "\n";
    }
    
    cout << str;
    
    return 0;
}
