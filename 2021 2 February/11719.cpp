#include <iostream>
#include <string>

using namespace std;

int main(){
    int i;
    string arr[100];
    
    for (i = 0; i < 100; i++){
        getline(cin, arr[i]);
        cout << arr[i] << endl;
    }
    
    return 0;
}
