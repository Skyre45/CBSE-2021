// Two tosses of a die, success = number greater than 5: histogram of the number of successes (0..2)
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    long N = 1000000, cnt[3] = {0};
    srand(1);
    for (long i = 0; i < N; i++) {
        int s = 0;
        for (int d = 0; d < 2; d++)
            if (rand() % 6 + 1 > 5) s++;
        cnt[s]++;
    }
    FILE *f = fopen("cbXIIq26b.dat", "w");
    for (int k = 0; k < 3; k++)
        fprintf(f, "%d %.6f\n", k, (double)cnt[k] / N);
    fclose(f);
    return 0;
}
