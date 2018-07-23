#include <stdio.h>

int arr[1000001];

void make(int x){
	arr[1] = 0;
	arr[2] = 1;
	arr[3] = 1;

	int i;
	for(i = 4; i <= x; i++){
		arr[i] = arr[i-1] + 1;
		if(i%2 == 0){
			if(arr[i] > arr[i/2] + 1)
				arr[i] = arr[i/2] + 1;
		}
		if(i%3 == 0){
			if(arr[i] > arr[i/3] + 1)
				arr[i] = arr[i/3] + 1;
		}
	}
	printf("%d" , arr[x]);
}
int main(){
	int n;
	scanf("%d" , &n);
	make(n);
	return 0;
}