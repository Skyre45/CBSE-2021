// Area between x = y^2 and x = 4 split equally by x = a.
// A(a) = integral over y in [-sqrt(a), sqrt(a)] of (a - y^2) dy by the trapezoidal rule (difference equation),
// and a is found by bisection on A(a) - A(4)/2 = 0.
#include <stdio.h>
#include <math.h>

static double area(double a)
{
    int n = 2000;
    double h = 2.0 * sqrt(a) / n, A = 0.0;
    for (int k = 0; k < n; k++) {
        double y0 = -sqrt(a) + k * h, y1 = y0 + h;
        A += 0.5 * h * ((a - y0 * y0) + (a - y1 * y1));
    }
    return A;
}

int main(void)
{
    double total = area(4.0), lo = 0.1, hi = 4.0;
    for (int i = 0; i < 60; i++) {
        double mid = 0.5 * (lo + hi);
        if (area(mid) < total / 2.0) lo = mid; else hi = mid;
    }
    double a = 0.5 * (lo + hi);
    printf("total area = %.6f (32/3 = %.6f)\n", total, 32.0 / 3.0);
    printf("a = %.10f   4^(2/3) = %.10f\n", a, pow(4.0, 2.0 / 3.0));
    FILE *f = fopen("cbXIIq35a.dat", "w");
    fprintf(f, "%.10f\n", a);
    fclose(f);
    return 0;
}
