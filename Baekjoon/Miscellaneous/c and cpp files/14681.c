#include <stdio.h>

int main(){
    int a, b;
    
    scanf("%d %d", &a, &b);
    
    if (a < 0){
        if (b < 0){
            printf("%d", 3);
        } else if (b > 0) {
            printf("%d", 2);
        }
    } else {
        if (b < 0){
            printf("%d", 4);
        } else if (b > 0) {
            printf("%d", 1);
        }
    }
    
    return 0;
    
}
