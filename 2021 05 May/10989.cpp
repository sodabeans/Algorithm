#include <iostream>

using namespace std;

int arr[10001];

int main(){
    int i;
    int temp, n = 0;
    int max = 1;
    scanf("%d", &n);
    
    for (i = 0; i < n; i++){
        scanf("%d", &temp);
        ++arr[temp];
        if (temp > max){
            max = temp;
        }
    }
    
    for (i = 1; i <= max; i++){
        while (arr[i]){
            printf("%d\n", i);
            arr[i]--;
        }
    }
    
    return 0;
}
