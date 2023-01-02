#include <stdio.h>

int main(){
    int i, h, w, n;
    int result, count, t;
    scanf("%d", &t);
    
    for (i=0; i<t; i++){
        scanf("%d %d %d", &h, &w, &n);
        result = 0;
        count = 1;
        
        while (1){
            if (n <= h && count == 1){
                result = n * 100 + count;
                break;
            } else if (n <= h && count > 1){
                result = n * 100 + count;
                break;
            } else {
                n -= h;
            }
            count++;
        };
        
        printf("%d\n", result);
    }
    
    
    return 0;
}
