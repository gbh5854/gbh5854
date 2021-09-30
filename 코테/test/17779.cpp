#include <stdio.h>
#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

long map[21][21];
long divided[21][21];
int N, flag = 0;
long ans = 999999;

typedef struct draw{
    int r;
    int c;
    int d1;
    int d2;
}draw;

queue <draw> q;

void print_map(){
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){
            printf("%ld ", map[i][j]);
        }
        printf("\n");
    }    
}

void print_div(){
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){
            printf("%ld ", divided[i][j]);
        }
        printf("\n");
    }    
}

void initialize(){
    scanf("%d", &N);
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){
            scanf("%ld", &map[i][j]);
        }
    }
}

void draw_line(int r, int c, int d1, int d2){
    memset(divided, 0, sizeof(divided));
    divided[r][c] = 5;
    for(int i = 1; i <= d1; i++){
        divided[r+i][c-i] = 5;
        divided[r+d2+i][c+d2-i] = 5;
    }
    for(int i = 1; i <= d2; i++){
        divided[r+i][c+i] = 5;
        divided[r+d1+i][c-d1+i] = 5;
    }

    for(int i = 1; i < r + d1; i++){
        for(int j = 1; j <= c; j++){                        //area 1
            if(divided[i][j] != 5) divided[i][j] = 1;
            else break;
        }
    }
    for(int i = 1; i <= r + d2; i++){
        for(int j = N; j > c; j--){                        //area 2
            if(divided[i][j] != 5) divided[i][j] = 2;
            else break;
        }
    }
    for(int i = r+d1; i <= N; i++){
        for(int j = 1; j < c-d1+d2; j++){                        //area 3
            if(divided[i][j] != 5) divided[i][j] = 3;
            else break;
        }
    }
    for(int i = r+d2+1; i <= N ; i++){
        for(int j = N; j >= c-d1+d2; j--){                        //area 4
            if(divided[i][j] != 5) divided[i][j] = 4;
            else break;
        }
    }
}

void calculate(){
    long max = 0, min = 999999, diff = 0;
    long p[6] = {0};

    for(int r = 1; r <= N; r++){
        for(int c = 1; c <= N; c++){
            switch(divided[r][c]){
                case 0:
                    p[5]+= map[r][c];
                    break;
                case 1:
                    p[1] += map[r][c];
                    break;
                case 2:
                    p[2] += map[r][c];
                    break;
                case 3:
                    p[3] += map[r][c];
                    break;
                case 4:
                    p[4] += map[r][c];
                    break;
                case 5:
                    p[5] += map[r][c];
                    break;
            }
        }
    }

    for(int i = 1; i <= 5; i++){
        if(p[i] > max) max = p[i];
        if(p[i] < min) min = p[i];
    }

    // printf("\np[] = ");
    // for(int i = 1; i <= 5; i++){
    //     printf("%d ", p[i]);
    // }
    // printf("\n");

    diff = max - min;
    // printf("max = %ld min = %ld diff = %ld\n", max, min, diff);
    if(diff < ans){
        ans = diff;
        // print_div();
    }
}

void divide(){
    int d1_max, d2_max;
    for(int i = 1; i <= N-2; i++){
        for(int j = 1; j <= N; j++){
            d1_max = j - 1;
            d2_max = N - j;

            for(int k = 1; k <= d1_max; k++){
                for(int l = 1; l <= d2_max; l++){
                    if(i + k + l <= N && j - k >= 1 && j + l <= N){      //경계선이 올바르면
                        draw_line(i,j,k,l);
                        calculate();     
                    }
                }
            }
        }
    }
}

int main(){
    initialize();
    divide();
    printf("%ld", ans);
    return 0;
}