#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

int map[10][10];
int visited[10][10];
int score = 0;

void print_visited(){
    int i,j;
    for(i = 0; i < 4; i++){
        for(j = 0; j < 10; j++){
            printf("%d ", visited[i][j]);
            if(j == 3) printf(" ");
        }
        printf("\n");
    }
    printf("\n");
    for(i = 4; i < 10; i++){
        for(j = 0; j  <4; j++){
            printf("%d ", visited[i][j]);
        }
        printf("\n");
    }

    printf("\n");
}

void print_map(){
    int i,j;
    for(i = 0; i < 4; i++){
        for(j = 0; j < 10; j++){
            printf("%d ", map[i][j]);
            if(j == 3) printf(" ");
        }
        printf("\n");
    }
    printf("\n");
    for(i = 4; i < 10; i++){
        for(j = 0; j  <4; j++){
            printf("%d ", map[i][j]);
        }
        printf("\n");
    }

    printf("\n");
}

void cal_score(){
    int i,j;
    i = 6;
    while(i < 10){           //blue board row check
        int flag = 1;
        for(j = 0 ; j < 4; j++){
            if(map[j][i] != 1) {
                flag = 0;
                break;
            }
        }
        if(flag == 1){              //row full
            score++;
            for(j = 0; j < 4; j++){
                map[j][i] = 0;      //erase row
            }

            for(int k = 0; k < 4; k++){
                int idx = 1;
                for(j = i-1; j > 3; j--){       //move block
                    if(map[k][j] == 1){
                        break;
                    }else{
                        idx++;
                    }
                }

                if(j != 3){
                    int end_idx = j;
                    while(1){
                        if(map[k][end_idx] == 1 || end_idx == 10){
                            end_idx--;
                            break;
                        }
                        end_idx++;
                    }
                    for(int l = end_idx; l > j; l++){
                        for(int m)
                    }
                }
            }
            // for(int x = 0; x < 4; x++){
            //     for(int y = i; y > 6 ; y--){
            //         map[x][y] = map[x][y-1];
            //     }
            //     map[x][6]  = 0;     //clear new row
            // }

            i = 6;                  //search at first
        }else{
            i++;
        }
    }

    for(i = 6; i < 10; i++){            //green board column check
        int flag = 1;
        for(j = 0 ; j < 4; j++){
            if(map[i][j] != 1) {
                flag = 0;
                break;
            }
        }
        if(flag == 1){              //row full -> erase
            score++;
            for(int x = 0; x < 4; x++){
                for(int y = i; y > 6 ; y--){
                    map[x][y] = map[x][y-1];
                }
                map[x][6]  = 0;     //clear new row
            }
        }
    }   
}

void start(){
    int t,x,y, idx_x, idx_y;
    scanf("%d %d %d", &t, &x, &y);

    switch(t){
        case 1:
            idx_x = x+1;
            idx_y = y+1;

            while(1){            //move block(blue board)
                if(idx_y == 10 || map[x][idx_y] == 1){
                    break;
                }
                idx_y++;
            }
            map[x][idx_y-1] = 1;

            while(1){               //move block(green board)
                if(idx_x == 10 || map[idx_x][y] == 1){
                    break;
                }
                idx_x++;
            }
            map[idx_x-1][y] = 1;
            break;
        case 2:
            // map[x][y+1] = 1;
            // map[x][y] = 1;
            idx_x = x+1;
            idx_y = y+2;
            while(1){            //move block(blue board)
                if(idx_y == 10 || map[x][idx_y] == 1){
                    break;
                }
                idx_y++;
            }
            map[x][idx_y-1] = 1;
            map[x][idx_y-2] = 1;

            while(1){               //move block(green board)
                if(idx_x == 10 || map[idx_x][y] == 1 || map[idx_x][y+1] == 1){
                    break;
                }
                idx_x++;
            }
            map[idx_x-1][y] = 1;
            map[idx_x-1][y+1] = 1;
            break;
            break;
        case 3:
            // map[x][y] = 1;
            // map[x+1][y] = 1;
            idx_x = x+2;
            idx_y = y+1;
            while(1){            //move block(blue board)
                if(idx_y == 10 || map[x][idx_y] == 1 || map[x+1][idx_y] == 1){
                    break;
                }
                idx_y++;
            }
            map[x][idx_y-1] = 1;
            map[x+1][idx_y-1] = 1;

            while(1){               //move block(green board)
                if(idx_x == 10 || map[idx_x][y] == 1){
                    break;
                }
                idx_x++;
            }
            map[idx_x-1][y] = 1;
            map[idx_x-2][y] = 1;
            break;
    }
    print_map();
    cal_score();
    print_map();

    // print_visited();
    // move();

}

void initialize(){
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) start();
}

int main(){
    // print_map();
    initialize();
    return 0;
}