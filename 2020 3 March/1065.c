#include <stdio.h>

int h(int n){
    int i;
    int a, b, c;
    int result = 99;
    
    for (i=100;i<=n;i++){
        a = i / 100; //백의 자리 hundreds
        b = (i % 100) / 10; // 십의 자리 tens
        c = (i % 100) % 10; //일의 자리 ones
        if (a - b == b - c){
            result++;
        }
    }
    
    return result;
}

int main(){
    int n;
    int result = 0;
    
    scanf("%d", &n);
    
    if (n<100){
        printf("%d", n);
    } else {
        result = h(n);
        printf("%d", result);
    }
    
    return 0;
}
