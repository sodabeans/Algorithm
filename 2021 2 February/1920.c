#include <stdio.h>

int compare(int n, int arr[], int num){
    int i;
    
    for (i = 0; i < n; i++){
        if (arr[i] == num){
            return 1;
        }
    }
    
    return 0;
}

int main(){
    int i = 0;
    int n = 0;
    int m = 0;
    scanf("%d", &n);
    int arr1[n];
    
    for (i = 0; i < n; i++){
        scanf("%d", &arr1[i]);
    }
    
    scanf("%d", &m);
    int num;
    
    for (i = 0; i < m; i++){
        scanf("%d", &num);
        printf("%d", compare(n, arr1, num));
    }
    
    return 0;
}
