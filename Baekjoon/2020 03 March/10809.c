#include <stdio.h>
#include <string.h>

int main (){
    char str[101];
    int i;
    int arr[26];
    
    for (i = 0; i < 26; i++){
        arr[i] = -1;
    }
    
    scanf("%s", str);
    
    for (i = 0; i < strlen(str); i++) {
        if (arr[str[i] - 97] == -1){
            arr[str[i] - 97] = i;
        }
    }
    
    for (i = 0; i < 26; i++){
        printf("%d ", arr[i]);
    }

    return 0;
}
