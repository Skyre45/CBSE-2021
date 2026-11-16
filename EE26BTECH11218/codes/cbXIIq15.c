// Three cards from a deck of 52 without replacement: histogram of the number of red cards (0..3)
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    long N = 1000000, cnt[4] = {0};
    int deck[52];
    for (int i = 0; i < 52; i++) deck[i] = i;          // cards 0..25 are red, 26..51 are black
    srand(1);
    for (long t = 0; t < N; t++) {
        int red = 0;
        for (int d = 0; d < 3; d++) {                  // partial Fisher-Yates shuffle: draw without replacement
            int j = d + rand() % (52 - d);
            int tmp = deck[d]; deck[d] = deck[j]; deck[j] = tmp;
            if (deck[d] < 26) red++;
        }
        cnt[red]++;
    }
    FILE *f = fopen("cbXIIq15.dat", "w");
    for (int k = 0; k < 4; k++)
        fprintf(f, "%d %.6f\n", k, (double)cnt[k] / N);
    fclose(f);
    return 0;
}
