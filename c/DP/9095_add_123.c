#include <stdio.h>

int main(){
	int arr[12] ,input[100], n, a,i,j ,max = 0;
	arr[1] = 1;
	arr[2] = 2;
	arr[3] = 4;
	scanf("%d" , &n);
	for(j = 1; j <= n; j++){
		scanf("%d" , &input[j]);
		if(input[j] > max)
			max = input[j];
	}
	for(i = 4; i <= max; i++){
		arr[i] = arr[i-1] + arr[i-2] + arr[i-3];
	}
	for(i = 1; i <= n; i++)
		printf("%d\n" , arr[input[i]]);
	return 0;
}