#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void star1() {

    FILE *file;
    file = fopen("input.in", "r");

    size_t len = 102;
    char input[len][len];
    int count = 0;

    while(count < len && fgets(input[count++], len, file));

    printf("count=%d\n", count);

    int low_points = 0;
    int grid[len-1][len-1];

    for(int i = 0; i < len-2; i++) { 
        for(int j = 0; j < len-2; j++) {
            if(input[i][j] - '0' >= 0 && input[i][j] - '0' <= 9) {
                grid[i][j] = input[i][j] - '0';
                printf("%d", grid[i][j]);
            }
        }
        printf("\n");
    }

    for(int i = 0; i < len-2; i++) {
        for(int j = 0; j < len-2; j++) {

            if (!i && !j && grid[i][j] < grid[i][j+1] && grid[i][j] < grid[i+1][j] &&
                    grid[i][j] < grid[i+1][j+1]) {
                low_points++;    
            } else if (!i && j < len-3 && grid[i][j] < grid[i][j-1] && 
                    grid[i][j] < grid[i][j+1] && grid[i][j] < grid[i+1][j-1] && 
                    grid[i][j] < grid[i+1][j] && grid[i][j] < grid[i+1][j+1]) {
                low_points++;
            } else if (!j && i < len-3 && grid[i][j] < grid[i-1][j] && 
                    grid[i][j] < grid[i-1][j+1] && grid[i][j] < grid[i][j+1] && 
                    grid[i][j] < grid[i+1][j] && grid[i][j] < grid[i+1][j+1]) {
                low_points++;
            } else if (i == len-3 && j == len-3 && grid[i][j] < grid[i-1][j-1] &&
                    grid[i][j] < grid[i-1][j] && grid[i][j] < grid[i][j-1]) {
                low_points++;
            } else if (i == len-3 && j && grid[i][j] < grid[i-1][j-1] && 
                    grid[i][j] < grid[i-1][j] && grid[i][j] < grid[i-1][j+1] && 
                    grid[i][j] < grid[i][j-1] && grid[i][j] < grid[i][j+1]) {
                low_points++;
            } else if (i && j == len-3 && grid[i][j] < grid[i-1][j-1] && 
                    grid[i][j] < grid[i-1][j] && grid[i][j] < grid[i][j-1] &&
                    grid[i][j] < grid[i+1][j-1] && grid[i][j] < grid[i+1][j]) {
                low_points++;
            } else if (i == len-3 && !j && grid[i][j] < grid[i-1][j] && 
                    grid[i][j] < grid[i-1][j+1] && grid[i][j] < grid[i][j+1]) {
                low_points++;
            } else if (!i && j == len-3 && grid[i][j] < grid[i][j-1] && 
                    grid[i][j] < grid[i+1][j-1] && grid[i][j] < grid[i+1][j]) {
                low_points++;
            } else if (grid[i][j] < grid[i-1][j-1] && grid[i][j] < grid[i-1][j] &&
                    grid[i][j] < grid[i-1][j+1] && grid[i][j] < grid[i][j-1] && 
                    grid[i][j] < grid[i][j+1] && grid[i][j] < grid[i+1][j-1] &&
                    grid[i][j] < grid[i+1][j] && grid[i+1][j+1])
                low_points++;
        }
    }

    printf("the number of low points is %d\n", low_points);
}

void star2() {

}

int main() {
    star1();
    star2();

    return 0;
}
