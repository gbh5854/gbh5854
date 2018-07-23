#include <stdio.h>

int main(){
	int arr[51][3];
	int n,m,i,j , min_set , min_one ,count = 0;
	
	scanf("%d %d" , &n , &m);
	for(i = 1; i <= m; i++){
		scanf("%d %d" , &arr[i][1] , &arr[i][2]);
	}
	min_set = arr[1][1];
	for(i = 2; i <= m; i++){
		if(min_set > arr[i][1])
			min_set = arr[i][1];
	}
	min_one = arr[1][2];
	for(i = 2; i <= m; i++){
		if(min_one > arr[i][2])
			min_one = arr[i][2];
	}
	if(n%6 == 0){
		if(min_set >= 6*min_one)
			count += min_one * n;
		else
			count += min_set * (n/6);
	}else{
		if(min_set >= 6*min_one)
			count += min_one * n;
		else{
			if(min_set >= (n%6) * min_one)
				count += (min_set * (n/6)) + min_one *(n%6);
			else
				count += min_set * ((n/6) + 1);
		}
	}
	printf("%d" , count);
	return 0;
}