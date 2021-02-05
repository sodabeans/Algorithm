#include <stdio.h>

int main(){
    int a, b, v;
    scanf("%d %d %d", &a, &b, &v);
    
    int days = (v - b - 1) / (a - b);
    
    printf("%d", days + 1);
    
    return 0;
}
