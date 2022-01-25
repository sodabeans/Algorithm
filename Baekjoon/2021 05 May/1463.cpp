// 시간초과 문제 해결 방법: cin cout은 입출력이 많을 때 시간이 많이 걸린다!

#include <iostream>
#include <algorithm>

using namespace std;

void search(int* A, int n, int num){
    int low = 0;
    int high = n - 1;
    int mid = (low + high) / 2;
    
    while(low <= high){
        mid = (low + high) / 2;
        if (num == A[mid]){
            printf("1\n");
            break;
        } else if (num < A[mid]){
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    
    if (low > high && A[mid] != num){
        printf("0\n");
    }
}

int main(){
    int i, n, m, input = 0;
    scanf("%d", &n);
    
    int A[n];
    for (i = 0; i < n; i++){
        scanf("%d", &A[i]);
    }
    
    sort(A, A + n);
    
    cin >> m;
    for (i = 0; i < m; i++){
        scanf("%d", &input);
        search(A, n, input);
    }
    
    return 0;
}
