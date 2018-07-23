#include <stdio.h>
#include <stdlib.h>

int main(){
	int i,n,arr[1001];
	scanf("%d" , &n);
	for(i = 1; i <= n; i++){
		scanf("%d" , &arr[i]);
	}
	for(i = 1; i <=n; i++)
		printf("%d " , arr[i]);
	return 0;
}