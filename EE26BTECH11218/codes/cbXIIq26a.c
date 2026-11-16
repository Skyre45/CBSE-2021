// Two tickets from 1..19 without replacement: histogram of the number of even tickets (0..2)
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    long N = 1000000, cnt[3] = {0};
    int t[19];
    for (int i = 0; i < 19; i++) t[i] = i + 1;
    srand(1);
    for (long r = 0; r < N; r++) {
        int ev = 0;
        for (int d = 0; d < 2; d++) {
            int j = d + rand() % (19 - d);
            int tmp = t[d]; t[d] = t[j]; t[j] = tmp;
            if (t[d] % 2 == 0) ev++;
        }
        cnt[ev]++;
    }
    FILE *f = fopen("cbXIIq26a.dat", "w");
    for (int k = 0; k < 3; k++)
        fprintf(f, "%d %.6f\n", k, (double)cnt[k] / N);
    fclose(f);
    return 0;
}
