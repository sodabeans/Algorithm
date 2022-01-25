//어려웠던 문제

#include <stdio.h>

int arr[2187][2187];

void setStar(int a, int b, int size){
    if(size == 1){
        arr[a][b] = '*';
        return;
    }
    
    int i, j;
    int count = 0;
    int temp = size/3;
    
    for (i=0; i<3; i++){
        for (j=0; j<3; j++){
            count++;
            if (count != 5){
                setStar(a+i*temp, b+j*temp, temp);
            }
        }
    }
}


int main(){
    int n, i, j;
    scanf("%d", &n);

    for (i=0; i<n; i++){
        for (j=0; j<n; j++){
            arr[i][j] = ' ';
        }
    }
    
    setStar(0,0,n);
    
    for (i=0; i<n; i++){
        for (j=0; j<n; j++){
            printf("%c", arr[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
