#include <iostream>
#include <algorithm>

using namespace std;
unsigned int arr[500001];

void compare(unsigned int* A, unsigned int x, int high){
    int low = 0;
    int mid = 0;
    
    while(low <= high){
        mid = (low + high) / 2;
        if (x == A[mid]){
            printf("1 ");
            break;
        } else if (x < A[mid]){
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    
    if (low > high && A[mid] != x){
        printf("0 ");
    }
}

int main(){
    int i = 0;
    int m, n;
    scanf("%d", &n);
    
    for (i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    sort(arr, arr + n);
    
    scanf("%d", &m);
    unsigned int input;
    
    for (i = 0; i < m; i++){
        scanf("%d", &input);
        compare(arr, input, n);
    }
    
    return 0;
}
