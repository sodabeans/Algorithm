#include <iostream>

using namespace std;

int factorial (int number){
    int answer = 1;
    if (number != 0){
        for (int i = 0; i < number; i++){
            answer *= (number - i);
        }
    }
    return answer;
}

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k;
    cin >> n >> k;
    
    cout << factorial(n) / (factorial(k) * factorial(n-k));
    
    return 0;
}
