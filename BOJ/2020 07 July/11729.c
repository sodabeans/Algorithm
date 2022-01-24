#include <stdio.h>

int tower_cnt;

void tower(int c, int start, int end, int temp) {
    if (c == 1) {
        printf("%d %d\n", start, end);
        return;
    }

    tower((c - 1), start, temp, end);
    printf("%d %d\n", start, end);

    tower((c - 1), temp, end, start);
    
}

void count(int c, int start, int end, int temp){
    if (c <= 1) {
        tower_cnt++;
        return;
    }

    count(c - 1, start, temp, end);
    tower_cnt++;
    count(c - 1, temp, end, start);
}

int main(void) {

    int c;
    scanf("%d", &c);
    
    tower_cnt = 0;
    count(c, 1, 3, 2);
    printf("%d\n", tower_cnt);
    tower(c, 1, 3, 2);

    return 0;

}


