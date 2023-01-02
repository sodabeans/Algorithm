#include <stdio.h>

int main(){
    int x[3];
    int y[3];
    int i, x_out, y_out;
    
    for (i=0; i<3; i++){
        scanf("%d %d", &x[i], &y[i]);
    }
    
    if(x[0] != x[1] && x[0] != x[2]){
        x_out = x[0];
    } else if (x[0] != x[1] && x[1] != x[2]){
        x_out = x[1];
    } else {
        x_out = x[2];
    }
    
    if(y[0] != y[1] && y[0] != y[2]){
        y_out = y[0];
    } else if (y[0] != y[1] && y[1] != y[2]){
        y_out = y[1];
    } else {
        y_out = y[2];
    }
    
    printf("%d %d", x_out, y_out);
    
    return 0;
}
