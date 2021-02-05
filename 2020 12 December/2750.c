#include <stdio.h>

int main(){
    int i, j;
    int temp = 0;
    int n = 0;
    scanf("%d", &n);
    
    int arr[n];
    
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            if (arr[i] < arr[j]){
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
    
    for(i = 0; i < n; i++){
        printf("%d\n", arr[i]);
    }
    
    return 0;
}
