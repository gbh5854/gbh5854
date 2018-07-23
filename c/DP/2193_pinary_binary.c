#include <stdio.h>

int main(){
	int n,i,j; 
	long long arr[91][2];
	long long dp[91];
	scanf("%d" , &n);
	dp[1] = 1 , dp[2] = 1;
	for(i = 3; i <= n; i++)
		dp[i] = dp[i-1] + dp[i-2];
	
	// arr[0][0] = 0, arr[0][1] = 1;
	// for(i = 1; i <= n; i++){
	// 	arr[i][0] = arr[i-1][0] + arr[i-1][1];
	// 	arr[i][1] = arr[i-1][0];
	// }
	

	// for(i = 0; i <= n; i++){
	// 	printf("%lld %lld\n" , arr[i][0] , arr[i][1]);
	// }
	// printf("%lld" , arr[n][0] + arr[n][1]);
	
	// for(i = 1; i <= n; i++){
	// 	printf("%lld  " , dp[i]);
	// }
	printf("%lld" , dp[n]);
	return 0;
}