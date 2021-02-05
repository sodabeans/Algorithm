#include <stdio.h>

int main(){
    int i;
    int cnt1 = 0;
    int cnt2 = 0;
    
    int arr[8];
    for (i=0; i<8; i++){
        scanf("%d", &arr[i]);
    }
    
    for (i=1; i<8; i++){
        if (arr[i] == arr[i-1] + 1){
            cnt1++;
        }
        if (arr[i] == arr[i-1] - 1){
            cnt2++;
        }
    }
    
    if (cnt1 == 7){
        printf("ascending");
    }else if (cnt2 == 7){
        printf("descending");
    } else {
        printf("mixed");
    }
    
    return 0;
}
