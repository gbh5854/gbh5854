#include <stdio.h>
int rule[4][1025];
int map[101][101];

void calculate_curve(){
	int j,i;
	for(j = 0; j < 4; j++){
		rule[j][1] = j;
		int a = 1, cal,x, back;
		for(i = 1; i <= 10; i++){
			int x;
			int tmp = a;				
			a *= 2;					
			cal = a - tmp;			
			
			for(x = cal + 1; x <= a; x++){
				if(rule[j][cal] == 3){
					rule[j][x] = 0;
				}
				else{
					rule[j][x] = rule[j][cal] + 1;
				}
				cal--;
			}
		}
	}
}

int findsuqare(){
	int i,j,cnt = 0;
	for(i = 0; i <= 99; i++){
		for(j = 0; j <= 99; j++){
			if(map[i][j] == 1 && map[i][j+1] == 1 && map && map[i+1][j+1] == 1 && map[i+1][j] == 1)
				cnt++;
		}
	}
	return cnt;
}

int main(){
	int n,i,j,arr[21][5];
	scanf("%d" , &n);
	for(i = 1; i <= n; i++){
		for(j = 1; j <= 4; j++)
			scanf("%d" , &arr[i][j]);
	}
	calculate_curve();
	for(i = 1; i <= n; i++){
		int x = arr[i][1] , y = arr[i][2] , count = 1;
		map[y][x] = 1;
		for(j = 1; j <= arr[i][4]; j++)
			count *= 2;
		for(j = 1; j <= count; j++){
			if(rule[arr[i][3]][j] == 0){		//dir0 : x+
				map[y][x+1] = 1;
				x+=1;
			}else if(rule[arr[i][3]][j] == 1){		//dir1 : y-
				map[y-1][x] = 1;
				y-=1;
			}else if(rule[arr[i][3]][j] == 2){
				map[y][x-1] = 1;
				x-=1;
			}else{
				map[y+1][x] = 1;
				y+=1;
			}
		}
	}
	printf("%d" , findsuqare());
	return 0;
}