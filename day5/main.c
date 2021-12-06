#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void star1() {

    FILE * file = fopen("input.in", "r");
    size_t len = 64;
    char vents[len];

    char floor[1000][1000];
    for(int i = 0; i < 1000; i++) {
        for(int j = 0; j < 1000; j++)
            floor[i][j] = 0;
    }

    while(fgets(vents, len, file)) {

        char num[4];
        for(int i = 0; i < 4; i++) {
            num[i] = '\0';
        }

        int count = -1;
        while(vents[++count] != ',');

        memcpy(num, vents, count);
        int x1 = atoi(num);

        //printf("x1 is %d\n", x1);

        int start_x2 = ++count;
        while(vents[++count] != '-');

        memcpy(num, vents + start_x2, count - start_x2 - 1);
        int y1 = atoi(num);

        //printf("y1 is %d\n", y1);
        
        int start_x3 = count + 3;
        while(vents[++count] != ',');

        memcpy(num, vents + start_x3, count - start_x3);
        int x2 = atoi(num);

        //printf("x2 is %d\n", x2);
        
        int start_x4 = ++count;
        while(vents[++count] != '\n');

        memcpy(num, vents + start_x4, count - start_x4);
        int y2 = atoi(num);

        //printf("y2 is %d\n", y2);
    
        int x_max = x1 > x2 ? x1 : x2;
        int x_min = x1 < x2 ? x1 : x2;

        int y_max = y1 > y2 ? y1 : y2;
        int y_min = y1 < y2 ? y1 : y2;

        for(int i = x_min; i <= x_max; i++) {
            for(int j = y_min; j <= y_max; j++)
                floor[i][j]++;
        }
    }

    int overlap = 0;
    for(int i = 0; i < 1000; i++) {
        for(int j = 0; j < 1000; j++) {
            printf("%d ", floor[i][j]);
            if(floor[i][j] >= 2)
                overlap++;
        }
        printf("\n");
    }

    printf("the number of at least 2 overlaps is %d\n", overlap);
}

void star2() {

}

int main() {

    star1();
    star2();
    return 0;
}

