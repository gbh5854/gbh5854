#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef struct shark{
    int r;
    int c;
    int speed;
    int dir;
    int size;
}shark;

shark map[101][101];
int R,C,M, fisher, ans = 0;
queue <shark> q;

void print_queue(){
    printf("queue size : %d\n", q.size());
    int size = q.size();
    for(int i = 0; i < size; i++){
        shark tmp;
        tmp.r = q.front().r;
        tmp.c = q.front().c;
        tmp.speed = q.front().speed;
        tmp.dir = q.front().dir;
        tmp.size = q.front().size;
        printf("(%d %d %d %d %d)\n", tmp.r,tmp.c,tmp.speed,tmp.dir,tmp.size);
        q.pop();
        q.push(tmp);
    }
}

void print_map_speed(){
    for(int i = 1; i <= R; i++){
        for(int j = 1; j <= C; j++){
            printf("%d ", map[i][j].speed);
        }
        printf("\n");
    }
}

void print_map_dir(){
    for(int i = 1; i <= R; i++){
        for(int j = 1; j <= C; j++){
            printf("%d ", map[i][j].dir);
        }
        printf("\n");
    }
}

void print_map_size(){
    for(int i = 1; i <= R; i++){
        for(int j = 1; j <= C; j++){
            printf("%d ", map[i][j].size);
        }
        printf("\n");
    }
}

void inttialize(){
    scanf("%d %d %d", &R, &C, &M);
    for(int i = 1; i <= M; i++){
        shark tmp;
        int tmp_r, tmp_c;
        scanf("%d %d %d %d %d", &tmp_r, &tmp_c, &tmp.speed, &tmp.dir, &tmp.size);
        map[tmp_r][tmp_c] = tmp;
        tmp.r = tmp_r;
        tmp.c = tmp_c;
        q.push(tmp);
    }
}

void catch_shark(){
    fisher++;
    for(int i = 1; i <= R; i++){
        if(map[i][fisher].size != 0){
            ans += map[i][fisher].size;

            map[i][fisher].r = 0;
            map[i][fisher].c = 0;
            map[i][fisher].speed = 0;
            map[i][fisher].dir = 0;
            map[i][fisher].size = 0;
            break;
        }
    }
}

void move(shark * tmp){
    int m;
    int dir = tmp->dir;
    if(dir <= 2) m = tmp->speed % ((2*R) -2);
    else m = tmp->speed % ((2*C) -2);

    for(int i = 0; i < m; i++){
        if(dir <= 2){
            if(tmp->r == 1) dir = 2;
            if(tmp->r == R) dir = 1;            
        }else{
            if(tmp->c == 1) dir = 3;
            if(tmp->c == C) dir = 4;
        }


        if(dir == 1) tmp->r -= 1;
        else if(dir == 2) tmp->r += 1;
        else if(dir == 3) tmp->c += 1;
        else tmp->c -= 1;

        tmp->dir = dir;
    }
}

void shark_move(){
    shark tmp;
    size = q.size();
    for(int i = 0; i < size; i++){
        tmp.r = q.front().r;
        tmp.c = q.front().c;
        tmp.speed = q.front().speed;
        tmp.dir = q.front().dir;
        tmp.size = q.front().size;
        q.pop();

        if(map[tmp.r][tmp.c].size != 0){
            move(&tmp);
            q.push(tmp);
        }
    }
}

void clear_map(){
    for(int i = 1; i <= R; i++){
        for(int j = 1; j <= C; j++){
            map[i][j].r = 0;
            map[i][j].c = 0;
            map[i][j].speed = 0;
            map[i][j].dir = 0;
            map[i][j].size = 0;
        }
    }
}

void update_map(){
    shark tmp;
    clear_map();
    int size = q.size();
    for(int i = 0; i < size; i++){
        tmp.r = q.front().r;
        tmp.c = q.front().c;
        tmp.speed = q.front().speed;
        tmp.dir = q.front().dir;
        tmp.size = q.front().size;
        q.pop();

        if(map[tmp.r][tmp.c].size != 0){        //shark exist
            if(map[tmp.r][tmp.c].size < tmp.size){
                map[tmp.r][tmp.c] = tmp;
            }
        }else{
            map[tmp.r][tmp.c] = tmp;
        }
    }
}

void update_queue(){
    queue <shark> tmpq;
    swap(q,tmpq);
    shark tmp;
    for(int i = 1; i <= R; i++){
        for(int j = 1; j <= C; j++){
           if(map[i][j].size != 0){
               tmp.r = map[i][j].r;
               tmp.c = map[i][j].c;
               tmp.speed = map[i][j].speed;
               tmp.dir = map[i][j].dir;
               tmp.size = map[i][j].size;
               q.push(tmp);
           }
        }
    }
}

int main(){
    inttialize();
    // print_map_size();
    while(fisher <= C){
        catch_shark();
        // print_queue();
        // print_map_size();
        shark_move();
        // print_queue();
        // print_map_size();
        update_map();
        update_queue();
        // print_queue();
        // print_map_size();
    }
    printf("%d", ans);
    return 0;
}