// Bag 1: 5 red, 4 black; bag 2: 3 red, 6 black. Choose a bag at random, draw two balls without replacement.
// Estimate P(B = b | both balls red) from the trials in which both balls are red.
#include <stdio.h>
#include <stdlib.h>

static double unif(void) { return rand() / (RAND_MAX + 1.0); }

int main(void)
{
    long N = 4000000, both = 0, from[3] = {0, 0, 0};
    srand(1);
    for (long i = 0; i < N; i++) {
        int b = rand() % 2 + 1;
        double r = (b == 1) ? 5.0 : 3.0;               // red balls in the chosen bag (9 balls in all)
        int first = unif() < r / 9.0;
        int second = unif() < (first ? r - 1.0 : r) / 8.0;
        if (first && second) { both++; from[b]++; }
    }
    FILE *f = fopen("cbXIIq32.dat", "w");
    for (int b = 1; b <= 2; b++)
        fprintf(f, "%d %.6f\n", b, (double)from[b] / both);
    fclose(f);
    return 0;
}
