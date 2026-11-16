// Euler forward-difference method for x y' - y = log x, y(1) = 1:  y_{k+1} = y_k + h (y_k + log x_k) / x_k
#include <stdio.h>
#include <math.h>

static double exact(double x) { return -log(x) - 1.0 + 2.0 * x; }    // C = 2

int main(void)
{
    double hs[4] = {0.1, 0.05, 0.025, 0.0125};
    printf("   h      error at x = 5\n");
    for (int i = 0; i < 4; i++) {
        int n = (int)(4.0 / hs[i] + 0.5);
        double x = 1.0, y = 1.0;
        for (int k = 0; k < n; k++) {
            y += hs[i] * (y + log(x)) / x;
            x += hs[i];
        }
        printf("%-8g %.5f\n", hs[i], fabs(y - exact(5.0)));
    }
    FILE *out = fopen("cbXIIq14.dat", "w");               // h = 0.01, every step
    double h = 0.01, x = 1.0, y = 1.0, emax = 0.0;
    fprintf(out, "%.4f %.6f\n", x, y);
    for (int k = 0; k < 400; k++) {
        y += h * (y + log(x)) / x;
        x = 1.0 + h * (k + 1);
        fprintf(out, "%.4f %.6f\n", x, y);
        if (fabs(y - exact(x)) > emax) emax = fabs(y - exact(x));
    }
    fclose(out);
    printf("h = 0.01: max |Euler - exact| = %.6f\n", emax);
    return 0;
}
