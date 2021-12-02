#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void star1() {

    int x=0, d=0;

    FILE *file;
    file = fopen("input.in", "r");

    size_t len = 100;
    char instr[len];
    
    while(fgets(instr, len, file)) {
        if (instr[0] == 'f') {
            int n = atoi(instr + 8);
            x += n;
        } else if (instr[0] == 'd') {
            int n = atoi(instr + 5);
            d += n;
        } else if (instr[0] == 'u') {
            int n = atoi(instr + 3);
            d -= n;
        }
    } 

    printf("star1=%d\n", x * d);
}

void star2() {

    int x=0, d=0, aim=0;

    FILE *file;
    file = fopen("input.in", "r");

    size_t len = 100;
    char instr[len];
    
    while(fgets(instr, len, file)) {
        if (instr[0] == 'f') {
            int n = atoi(instr + 8);
            x += n;
            d += aim * n;
        } else if (instr[0] == 'd') {
            int n = atoi(instr + 5);
            aim += n;
        } else if (instr[0] == 'u') {
            int n = atoi(instr + 3);
            aim -= n;
        }
    } 

    printf("star2=%d\n", x * d);
}

int main() {

    star1();
    star2();
    return 0;
}
