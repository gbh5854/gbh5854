#include <stdio.h>

int main(){
	int e,s,m,i=1;
	scanf("%d %d %d" , &e,&s,&m);
	if(e == 15)
		e = 0;
	if(s == 28)
		s = 0;
	if(m == 19)
		m = 0;
	while(1){
		if(i%15 == e && i%28 == s && i%19 == m)
			break;
		i++;
	}
	printf("%d" , i);
	return 0;
}