#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b){
    if (*(int*) a > *(int*) b){
        return 1;
    } else if (*(int*) a < *(int*) b){
        return -1;
    } else {
        return 0;
    }
}

int main(){
    int i;
    int n = 0;
    scanf("%d", &n);
    
    int arr[n];
    
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    
    qsort(arr, n, sizeof(int), compare);
    
    for(i = 0; i < n; i++){
        printf("%d\n", arr[i]);
    }
    
    return 0;
}
