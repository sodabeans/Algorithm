#include <stdio.h>
#include <string.h>

int main(){
    int i;
    int temp = 0;
    int result = -2;
    int arr[26] = {0};
    
    char str[1000001];
    scanf("%s", str);
    
    int length = strlen(str); //strlen을 for 안에 넣으면 loop 돌아갈때마다 length를 계산하게됨
    
    for (i = 0; i < length; i++){
        if (str[i] >= 'a' && str[i] <= 'z'){
            arr[str[i] - 97]++;
        } else {
            arr[str[i] - 65]++;
        }
    }
    
    for (i = 0; i < 26; i++){
        if (arr[i] > temp){
            temp = arr[i];
            result = i;
        } else if (arr[i] == temp){
            result = -2;
        }
    }
    
    printf("%c", result + 65);
    
    return 0;
}
