#include <stdio.h>

int main(){
    int min = 0;
    int hr = 0;
    
    scanf("%d %d", &hr, &min);
    
    min -= 45;
    
    if (min < 0){
        hr -= 1;
        min += 60;
    }
    
    if (hr < 0){
        hr += 24;
    }
    
    printf("%d %d", hr, min);
    
    return 0;
}
