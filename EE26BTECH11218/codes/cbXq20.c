// Cards numbered 1..20: X = number on the card drawn, uniform on {1,...,20}.
// Estimate P(Y=1) for the indicator random variables of the five events by simulation.
#include <stdio.h>
#include <stdlib.h>

static int is_prime(int n)
{
    if (n < 2) return 0;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0) return 0;
    return 1;
}

int main(void)
{
    long N = 1000000, c[5] = {0}, even = 0;
    srand(1);
    for (long i = 0; i < N; i++) {
        int x = rand() % 20 + 1;
        if (x > 2 && is_prime(x)) c[0]++;              // (i)   odd prime
        if (x > 1 && !is_prime(x)) c[1]++;             // (ii)  composite
        if (x % 18 == 0) c[2]++;                       // (iii) multiple of 3, 6 and 9
        if (x % 21 == 0) c[3]++;                       // (iv)  multiple of 3 and 7
        if (x % 2 == 0) {                              // (v)   odd cards removed: condition on X even
            even++;
            if (is_prime(x)) c[4]++;
        }
    }
    FILE *f = fopen("cbXq20.dat", "w");
    for (int k = 0; k < 4; k++)
        fprintf(f, "%d %.6f\n", k + 1, (double)c[k] / N);
    fprintf(f, "5 %.6f\n", (double)c[4] / even);
    fclose(f);
    return 0;
}
