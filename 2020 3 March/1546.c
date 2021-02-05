#include <stdio.h>

int main() {
    int n, i;
    double M = 0.0;
    double sum = 0;
    
    scanf("%d", &n);
    
    double arr[n];
    
    for (i=0;i<n;i++){
        scanf("%lf", &arr[i]);
        if (M < arr[i]){
            M = arr[i];
        }
    }
    
    for (i=0;i<n;i++){
        sum = sum + (arr[i]*100 / M);
    }
    
    printf("%0.2lf\n", sum / n);
    
    return 0;
}
