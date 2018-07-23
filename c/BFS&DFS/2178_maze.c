#include <stdio.h>
int i,j,M , N;
int map[501][501];
int visit[501][501];

typedef struct n{
	int x;
	int y;
}q;

q queue[10001];
int front , rear , max;

int vectX[4] = {0,0,1,-1};
int vectY[4] = {1,-1,0,0};

q deque();
void enque(int, int);
int isEmpty();

void bfs(){
	int nextX , nextY;
	while(isEmpty()){
		q pop = deque();
		for(i = 0; i < 4; i++){
			nextX = pop.x + vectX[i];
			nextY = pop.y + vectY[i];

			if(nextX >= 1 && nextX <= M && nextY >= 1 && nextY <= N){
				if(map[nextX][nextY] == 1 && visit[nextX][nextY] == 0){
					enque(nextX , nextY);
					visit[nextX][nextY] = visit[pop.x][pop.y] + 1;
				}
			}
		}
	}
}


int main(){
	scanf("%d %d" , &M, &N);
	for(i = 1; i <= M; i++){
		for(j = 1; j <= N; j++){
			scanf("%1d" , &map[i][j]);
		}
	}

	visit[1][1] = 1;
	enque(1,1);
	bfs();
	printf("%d" , visit[M][N]);
	return 0;
}

q deque(){
	q tmp = queue[front++];
	return tmp;
}

void enque(int x, int y){
	q tmp;
	tmp.x = x;
	tmp.y = y;
	queue[rear++] = tmp;
}

int isEmpty(){
	if(front == rear)
		return 0;
	else
		return 1;
}