// Three dice: simulate the sum of the three faces and count the outcomes with each sum
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    long N = 1000000, cnt[19] = {0};
    srand(1);
    for (long i = 0; i < N; i++) {
        int s = 0;
        for (int d = 0; d < 3; d++)
            s += rand() % 6 + 1;
        cnt[s]++;
    }
    FILE *f = fopen("cbXq16.dat", "w");
    for (int s = 3; s <= 18; s++)                      // frequency scaled to the 216 equally likely outcomes
        fprintf(f, "%d %.6f\n", s, (double)cnt[s] / N * 216.0);
    fclose(f);
    return 0;
}
