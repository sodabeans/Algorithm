#include <stdio.h>

int main(){
    long a, b, c;
    long n = 1;
    //long revenue = -1;
    
    scanf("%ld %ld %ld", &a, &b, &c);
    
    if(b >= c){
        printf("-1");
    } else {
        n = a / (c - b);
        /*while (revenue < 0){
            revenue = c * n - (a + b * n);
            n++;
        }*/
        printf("%ld", n+1);
    }
    
    return 0;
}
