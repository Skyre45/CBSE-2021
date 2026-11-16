// Two independent solvers: X_A ~ Bernoulli(1/3), X_B ~ Bernoulli(1/5); histogram of S = X_A + X_B
#include <stdio.h>
#include <stdlib.h>

static double unif(void) { return rand() / (RAND_MAX + 1.0); }

int main(void)
{
    long N = 1000000, cnt[3] = {0};
    srand(1);
    for (long i = 0; i < N; i++) {
        int s = (unif() < 1.0 / 3.0) + (unif() < 1.0 / 5.0);
        cnt[s]++;
    }
    FILE *f = fopen("cbXIIq1.dat", "w");
    for (int k = 0; k < 3; k++)
        fprintf(f, "%d %.6f\n", k, (double)cnt[k] / N);
    fclose(f);
    return 0;
}
