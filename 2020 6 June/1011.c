#include <stdio.h>

void func(long long length){
    long long count = 0;
    
    while (count * (count + 1) < length){
        count++;
    }
    
    if (count * count >= length){
        printf("%lld\n", 2 * count - 1);
    } else {
        printf("%lld\n", 2 * count);
    }

}

int main(){
    long long n, i;
    long long x, y, length;
    scanf("%lld", &n);
    
    for (i=0; i<n; i++){
        scanf("%lld %lld", &x, &y);
        length = y - x;
        func(length);
    }
    
    return 0;
}
