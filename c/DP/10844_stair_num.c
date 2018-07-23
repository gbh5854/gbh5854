#include <stdio.h>
int arr[101][10];
int sum = 0;
#define mod 1000000000
int main(){
	int n,i , j;
	for(i = 0; i <= 9; i++)
		arr[1][i] = 1;

	scanf("%d" , &n);
	for(i = 2; i <= n; i++){
		for(j = 0; j <= 9; j++){
			if(j == 0)
				arr[i][0] = arr[i-1][1] % mod;
			else if(j == 9)
				arr[i][9] = arr[i-1][8] % mod;
			else
				arr[i][j] = (arr[i-1][j-1] + arr[i-1][j+1]) % mod;
		}

	}
	for(i = 1; i <= 9; i++)
		sum = (sum + arr[n][i]) % mod;
	printf("%d" , sum);
	return 0;
}