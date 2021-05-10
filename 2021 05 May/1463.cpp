// 시간초과
#include <iostream>
#include <algorithm>

using namespace std;

int search(int* A, int num, int low, int high){
    int mid;
    
    while(low <= high){
        mid = (low + high) / 2;
        if (num == A[mid]){
            return 1;
        } else if (num < A[mid]){
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return 0;
}

int main(){
    int i, n, m, input, answer = 0;
    cin >> n;
    
    int A[n];
    for (i = 0; i < n; i++){
        cin >> A[i];
    }
    
    sort(A, A + n);
    int* B = A;
    
    cin >> m;
    for (i = 0; i < m; i++){
        cin >> input;
        answer = search(B, input, 0, n);
        cout << answer << "\n";
    }
    
    return 0;
}
