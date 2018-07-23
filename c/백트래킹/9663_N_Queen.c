#include <stdio.h>
#include <stdlib.h>

int arr[16];
int count=0, N;

int check(int x){
	int i;
	for(i = 1; i < x; i++){
		if(arr[i] == arr[x] || abs(arr[i] - arr[x]) == x - i)
			return 0;
	}
	return 1;
}

void queen(int x){
	int i;
	if(x == N){
		count++;
		return;
	}
	for(i = 1; i <= N; i++){
		arr[x+1] = i;
		if(check(x+1))
			queen(x+1);

	}
}
int main(){
	scanf("%d" , &N);
	queen(0);
	printf("%d" , count);
	return 0;
}