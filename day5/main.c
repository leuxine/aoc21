#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void clean(char * num) {
    for(int i = 0; i < 4; i++) {
        num[i] = '\0';
    }
}

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
        clean(num);

        int count = -1;
        while(vents[++count] != ',');

        memcpy(num, vents, count);
        int x1 = atoi(num);

        //printf("x1 is %d\n", x1);


        int start_x2 = ++count;
        while(vents[++count] != '-');

        clean(num);

        memcpy(num, vents + start_x2, count - start_x2 - 1);
        int y1 = atoi(num);

        //printf("y1 is %d\n", y1);
        
        int start_x3 = count + 3;
        while(vents[++count] != ',');

        clean(num);

        memcpy(num, vents + start_x3, count - start_x3);
        int x2 = atoi(num);

        //printf("x2 is %d\n", x2);
        
        int start_x4 = ++count;
        while(vents[++count] != '\n');

        clean(num);

        memcpy(num, vents + start_x4, count - start_x4);
        int y2 = atoi(num);

        //printf("y2 is %d\n", y2);

        if(x1 == x2) {

            int y_max = y1 > y2 ? y1 : y2;
            int y_min = y1 < y2 ? y1 : y2;

            for(int j = y_min; j <= y_max; j++)
                floor[j][x1]++;

        } else if (y1 == y2) {

            int x_max = x1 > x2 ? x1 : x2;
            int x_min = x1 < x2 ? x1 : x2;

            for(int i = x_min; i <= x_max; i++)
                floor[y1][i]++;

        }
    }

    int overlap = 0;
    for(int i = 0; i < 1000; i++) {
        for(int j = 0; j < 1000; j++) {
            if(floor[i][j] > 1)
                overlap++;
        }
    }

    printf("the number of at least 2 overlaps is %d\n", overlap);
}

void star2() {

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
        clean(num);

        int count = -1;
        while(vents[++count] != ',');

        memcpy(num, vents, count);
        int x1 = atoi(num);

        //printf("x1 is %d\n", x1);


        int start_x2 = ++count;
        while(vents[++count] != '-');

        clean(num);

        memcpy(num, vents + start_x2, count - start_x2 - 1);
        int y1 = atoi(num);

        //printf("y1 is %d\n", y1);
        
        int start_x3 = count + 3;
        while(vents[++count] != ',');

        clean(num);

        memcpy(num, vents + start_x3, count - start_x3);
        int x2 = atoi(num);

        //printf("x2 is %d\n", x2);
        
        int start_x4 = ++count;
        while(vents[++count] != '\n');

        clean(num);

        memcpy(num, vents + start_x4, count - start_x4);
        int y2 = atoi(num);

        //printf("y2 is %d\n", y2);

        if(x1 == x2) {

            int y_max = y1 > y2 ? y1 : y2;
            int y_min = y1 < y2 ? y1 : y2;

            for(int j = y_min; j <= y_max; j++)
                floor[j][x1]++;

        } else if (y1 == y2) {

            int x_max = x1 > x2 ? x1 : x2;
            int x_min = x1 < x2 ? x1 : x2;

            for(int i = x_min; i <= x_max; i++)
                floor[y1][i]++;

        } else {
            if ((x1 < x2) && (y1 < y2)) {
                for(int i = 0; i <= x2 - x1; i++)
                    floor[y1+i][x1+i]++;
            } else if ((x1 > x2) && (y1 > y2)) {
                for(int i = 0; i <= x1 - x2; i++)
                    floor[y1-i][x1-i]++;
            } else if ((x1 < x2) && (y1 > y2)) {
                for(int i = 0; i <= x2 - x1; i++)
                    floor[y1-i][x1+i]++;
            } else {
                for(int i = 0; i <= x1 - x2; i++)
                    floor[y1+i][x1-i]++;
            }
        }
    }

    int overlap = 0;
    for(int i = 0; i < 1000; i++) {
        for(int j = 0; j < 1000; j++) {
            if(floor[i][j] > 1)
                overlap++;
        }
    }

    printf("the number of at least 2 overlaps with diagonals is %d\n", overlap);
}

int main() {

    star1();
    star2();
    return 0;
}

