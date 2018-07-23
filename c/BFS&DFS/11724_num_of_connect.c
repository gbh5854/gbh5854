#include <stdio.h>
int Graph[1001][1001] = {0};
int DFSvisit[1001] = {0};

void DFS(int v, int N){
	int i;
	DFSvisit[v] = 1;
	for(i = 1;i <= N; i++){
		if(Graph[v][i] == 1 && DFSvisit[i] == 0)
			DFS(i , N);
	}
	return;
}

int main(){
	int N,M,i , x, y, count = 0;
	scanf("%d %d" , &N , &M);
	for(i = 0; i < M; i++){
		scanf("%d %d" , &x , &y);
		Graph[x][y] = 1;
		Graph[y][x] = 1;
	}
	count++;
	
	DFS(1,N);
	for(i = 1; i <= N; i++){
		if(DFSvisit[i] == 0){
			DFS(i,N);
			count++;
		}
	}
	printf("%d" , count);
	
	return 0;
}