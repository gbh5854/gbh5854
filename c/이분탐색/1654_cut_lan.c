#include <stdio.h>

int have[10001];
int make[10000001];
int K,N;
int count(int x){
	int i, num=0;
	for(i = 1; i <= K; i++){
		num += have[i] / x;
	}
	return num;
}
void cut(int left, int right , int x){
	if(count(right) == x){
		printf("%d" , right);
		return;
	}
	int m = (left + right) / 2;
	if(left == right){
		printf("%d" , left-1);
		return;
	}
	if(count(m) < x){
		cut(left , m , x);
	}else if(count(m) >= x){
		cut(m+1 , right, x);
	}
}
int main(){
	int i , max = 0;
	scanf("%d %d" , &K , &N);
	for(i = 1; i<= K;i++){
		scanf("%d" , &have[i]);
		if(max < have[i])
			max = have[i];
	}
	// printf("%d" , count(200));
	cut(1,max , N);

	return 0;
}