#include <stdio.h>

int main(void){
    int a = 1;

    printf("%u", -2 * a);
    printf("%u", (unsigned int)(-2) * a);
}