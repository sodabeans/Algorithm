#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i, n = 0;
    cin >> n;
    int arr[n];
    
    for (i = 0; i < n; i++){
        cin >> arr[i];
    }
    
    sort(arr, arr + n);
    
    cout << arr[0] << "\n";
    for (i = 1; i < n; i++){
        if (arr[i - 1] != arr[i]){
            cout << arr[i] << " ";
        }
    }
    
    return 0;
}
