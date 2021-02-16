#include <iostream>
#include <string>

using namespace std;

int main(){
    int x, y;
    cin >> x >> y;
    int totalDay = y;
    int i;
    
    for (i = 2; i <= x; i++){
        if (i == 3){
            totalDay += 28;
        } else if (i == 5 || i == 7 || i == 10 || i == 12){
            totalDay += 30;
        } else {
            totalDay += 31;
        }
    }
    
    switch (totalDay % 7){
        case 1:
            cout << "MON";
            break;
        case 2:
            cout << "TUE";
            break;
        case 3:
            cout << "WED";
            break;
        case 4:
            cout << "THU";
            break;
        case 5:
            cout << "FRI";
            break;
        case 6:
            cout << "SAT";
            break;
        case 0:
            cout << "SUN";
            break;
        default:
            break;
    }
    
    return 0;
}
