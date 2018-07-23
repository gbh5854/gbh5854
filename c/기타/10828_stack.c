#include <stdio.h>
#include <string.h>


typedef struct stack{
	int arr[10000];
	int top;
} Stack;

void stack_init(Stack * s){
	s -> top = -1;
}

int isEmpty(Stack * s){
	if(s -> top == -1)
		return 1;
	else
		return 0;
}

int size(Stack * s){
	return s -> top + 1;
}

int isFull(Stack * s){
	if(s -> top + 1 >= 10000)
		return 1;
	else
		return 0;
}

int pop(Stack *s){
	if(isEmpty(s))
		return -1;
	else{
		return s -> arr[(s -> top)--];
	}
}

void push(Stack *s , int n){
	s -> arr[++(s -> top)] = n;
	return;
}
int print_top(Stack *s){
	if(isEmpty(s))
		return -1;
	else
		return s -> arr[s -> top];
}
int main(){
	int n,i , num;
	char str[6];
	Stack stack;
	stack_init(&stack);
	scanf("%d" , &n);
	for(i = 0; i < n; i++){
		scanf("%s" , str);
		if(!strcmp(str , "push")){
			scanf("%d" , &num);
			push(&stack , num);
		}else if(!strcmp(str , "pop")){
			printf("%d\n" , pop(&stack));
		}else if(!strcmp(str , "empty")){
			printf("%d\n" , isEmpty(&stack));
		}else if(!strcmp(str , "size")){
			printf("%d\n" , size(&stack));
		}else if(!strcmp(str , "top")){
			printf("%d\n" , print_top(&stack));
		}
	}
	
	return 0;
}