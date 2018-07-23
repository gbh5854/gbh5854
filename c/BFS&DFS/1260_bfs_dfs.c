#include <stdio.h>

int Graph[1001][1001] = {0};
int DFSvisit[1001] = {0};
int BFSvisit[1001] = {0};
int queue[1001];

void DFS(int v, int N){
	int i;
	DFSvisit[v] = 1;
	printf("%d " , v);
	for(i = 1;i <= N; i++){
		if(Graph[v][i] == 1 && DFSvisit[i] == 0)
			DFS(i , N);
	}
	return;
}

void BFS(int v, int N){
	int front = 0, rear = 0, pop , i;
	
	printf("%d ", v);
	BFSvisit[v] = 1;
	queue[0] = v;
	rear++;

	while(front < rear){
		pop = queue[front];
		front++;

		for(i = 1; i <= N;i++){
			if(Graph[pop][i] == 1 && BFSvisit[i] == 0){
				queue[rear] = i;
				rear++;
				BFSvisit[i] = 1;
				printf("%d " , i);
			}
		}
	}
	return;
}


int main(){
	int N,M,Start;
	int i,x,y;

	scanf("%d %d %d" , &N, &M, &Start);
	for(i = 0; i < M; i++){
		scanf("%d %d" , &x , &y);
		Graph[x][y] = 1;
		Graph[y][x] = 1;
	}

	DFS(Start , N);
	printf("\n");
	BFS(Start , N);
	return 0;
}