#include <iostream>
#include <string>

using namespace std;

int main(){
    int n = 0;
    int i, j;
    cin >> n;
    
    for (i = 1; i <= n; i++){
        for (j = 1; j <= n - i; j++){
            cout << " ";
        }
        cout << "*";
        
        if (i == n){
            for (j = 1; j < (2 * n - 1); j++){
                cout << "*";
            }
        } else if (i != 1 && i != n){
            for (j = 1; j <= (2 * i - 3); j++){
                cout << " ";
            }
            cout << "*";
        }
        cout << "\n";
    }
    
    return 0;
}
