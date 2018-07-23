#include <stdio.h>

int main(){
	int n, k, i,coin,sum=0 , count;
	int arr[11];
	scanf("%d %d" , &n, &k);
	for(i= 1; i <= n; i++){
		scanf("%d" , &arr[i]);
	}
	while(1){
		coin = arr[i-1];
		count = k/coin;
		sum = sum + count;
		k = k - (count * arr[i-1]);
		if(k == 0)
			break;
		i--;
	}
	printf("%d" , sum);

	return 0;
}