#include <stdio.h>
int arr[1002][11];

int main(){
	int n,i,j;
	scanf("%d" , &n);
	for(i = 1; i <= 10; i++)
		arr[0][i] = 1;
	for(i = 1; i <= n; i++){
		arr[i][1] = 1;
		for(j = 2; j <= 10; j++){
			arr[i][j] = (arr[i][j-1] + arr[i-1][j]) % 10007;
		}
	}

	// for(i = 0; i <= n; i++){
	// 	for(j = 1; j <= 10; j++)
	// 		printf("%d\t" , arr[i][j]);
	// 	printf("\n");
	// }

	printf("%d" , arr[n][10]);
	return 0;
}