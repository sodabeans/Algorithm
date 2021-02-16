//very very very inefficient
//I just wanted to finish this problem quickly by copy and paste lol..

#include <iostream>
#include <string>

using namespace std;

int main(){
    int n, i, j;
    cin >> n;
    
    for (i = 1; i <= n; i++){
        for (j = 0; j < i; j++){
            cout << "*";
        }
        for (j = 0; j < n - i; j++){
            cout << " ";
        }
        for (j = 0; j < n - i; j++){
            cout << " ";
        }
        for (j = 0; j < i; j++){
            cout << "*";
        }
        cout << "\n";
    }
    
    for (i = n - 1; i > 0; i--){
        for (j = 0; j < i; j++){
            cout << "*";
        }
        for (j = 0; j < n - i; j++){
            cout << " ";
        }
        for (j = 0; j < n - i; j++){
            cout << " ";
        }
        for (j = 0; j < i; j++){
            cout << "*";
        }
        cout << "\n";
    }
    
    return 0;
}
