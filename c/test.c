#include <stdio.h>
#define mod 1000000000
int main(void){
    int N;
    int Dp[101][10] = {};
    int sum = 0;
    scanf("%d", &N);
    for (int i = 0; i < 10; i++)
        Dp[1][i] = 1;
    for (int i = 2; i <= N; i++){
        for (int j = 0; j < 10; j++){
            if (j == 0)
                Dp[i][0] = Dp[i - 1][1] % mod;
            else if (j == 9)
                Dp[i][9] = Dp[i - 1][8] % mod;
            else
                Dp[i][j] = (Dp[i - 1][j - 1] + Dp[i - 1][j + 1]) % mod;
        }
    }
    for (int i = 1; i < 10; i++)
        sum = (sum + Dp[N][i]) % mod;
    printf("%d\n", sum%mod);
}