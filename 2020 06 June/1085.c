#include <stdio.h>

int main(){
    int x, y, w, h, i;
    
    scanf("%d %d %d %d", &x, &y, &w, &h);
    
    int arr[5] = {x, y, };
    arr[2] = w-x;
    arr[3] = h-y;
    int min = x;
    
    for (i=1; i<4; i++){
        if (min > arr[i]){
            min = arr[i];
        }
    }
    
    printf("%d", min);
    
    return 0;
}
