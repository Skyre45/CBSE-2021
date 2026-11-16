// Trapezoidal rule as a difference equation for the improper integral of x/sqrt(1-x^2) on [0,b]:
//   A_0 = 0,  A_{k+1} - A_k = (h/2)(f(x_k) + f(x_{k+1}))
#include <stdio.h>
#include <math.h>

static double f(double x) { return x / sqrt(1.0 - x * x); }

int main(void)
{
    int n = 200000;
    double b[3] = {0.9, 0.99, 0.999};
    FILE *out = fopen("cbXIIq6.dat", "w");
    printf("   b        trapezoid        1 - sqrt(1-b^2)\n");
    for (int i = 0; i < 3; i++) {
        double h = b[i] / n, A = 0.0;
        for (int k = 0; k < n; k++)
            A += 0.5 * h * (f(k * h) + f((k + 1) * h));
        double exact = 1.0 - sqrt(1.0 - b[i] * b[i]);
        printf("%-8g %.6f        %.6f\n", b[i], A, exact);
        fprintf(out, "%g %.6f %.6f\n", b[i], A, exact);
    }
    fclose(out);
    return 0;
}
