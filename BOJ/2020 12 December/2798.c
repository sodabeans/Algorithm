#include <stdio.h>

int main(){
    int n = 0;
    int m, i, j, k;
    int sum = 0;
    int answer = 0;
    scanf("%d %d", &n, &m);
    int arr[n];
    
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    
    for(i = 0; i < n; i++){
        for(j = 1; j < n && j != i; j++){
            for(k = 2; k < n && k != i && k != j; k++){
                sum = arr[i] + arr[j] + arr[k];
                if (sum <= m && sum > answer){
                    answer = sum;
                    continue;
                }
            }
        }
    }
    
    printf("%d", answer);
    
    return 0;
}
