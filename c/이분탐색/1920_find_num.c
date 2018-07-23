#include <stdio.h>
#include <stdlib.h>

int arr[100001];
int find[100001];
int N,M;

int compare(void *first, void *second){
	if(*(int*)first > *(int*)second)
		return 1;
	else if(*(int*)first < *(int*)second)
		return -1;
	else
		return 0;
}

int findNum(int left , int right, int x){
	if(left == right){
		if(arr[left] == x)
			return 1;
		else
			return 0;
	}else{
		int m = (left + right) / 2;
		if( x < arr[m])
			return findNum(left, m,x);
		else if(x > arr[m])
			return findNum(m+1, right, x);
		else
			return 1;
	}
}
int main(){
	int i;
	int arr_size = sizeof(arr) / sizeof(int);

	scanf("%d" , &N);
	for(i = 1; i <= N; i++){
		scanf("%d" , &arr[i]);
	}
	
	scanf("%d" , &M);
	for(i = 1; i <= M; i++){
		scanf("%d" , &find[i]);
	}

	qsort(arr ,N+1 , sizeof(int) , compare);

	for(i = 1; i <= M; i++){
		printf("%d\n", findNum(1,N,find[i]));
	}
	return 0;
}