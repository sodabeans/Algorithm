#include <stdio.h>

int main(){
    int arr[10000];
    int n, i, j;
    
    arr[0] = 1;
    arr[1] = 1;
    
    for (i = 2; i <= 10000; i++){
        for (j = 2 * i; j <= 10000; j += i){
            arr[j] = 1;
        }
    }
    
    scanf("%d", &n);
    
    
    
    return 0;
}
