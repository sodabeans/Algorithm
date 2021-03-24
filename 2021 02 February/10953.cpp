#include <iostream>

using namespace std;

int main(){
    int count = 0;
    int i, a, b;
    char c;
    
    cin >> count;
    
    for (i = 0; i < count; i++){
        cin >> a >> c >> b;
        cout << a + b << "\n";
    }
    
    
    return 0;
}
