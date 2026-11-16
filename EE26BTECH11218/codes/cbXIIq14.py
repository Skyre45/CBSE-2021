# x y' - y = log x : closed form against the Euler forward-difference solution computed by the C program
import os
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")
mu = lambda x: 1 / x                                    # integrating factor
y_exact = lambda x, C: -np.log(x) - 1 + C * x           # (y/x)' = log(x)/x^2

xy = np.loadtxt(os.path.join(DIR, "cbXIIq14.dat"))      # columns: x_k, y_k  (h = 0.01, y(1) = 1)
xs, ys = xy[:, 0], xy[:, 1]
print("h = 0.01: max |Euler - exact| =", np.max(np.abs(ys - y_exact(xs, 2.0))))

# check that (mu*y)' = log(x)/x^2
x0, hh = 2.0, 1e-6
d = (mu(x0 + hh) * y_exact(x0 + hh, 2.0) - mu(x0 - hh) * y_exact(x0 - hh, 2.0)) / (2 * hh)
print("(mu y)' =", d, "  log(x)/x^2 =", np.log(x0) / x0 ** 2)

for C in [0, 1, 3]:
    plt.plot(xs, y_exact(xs, C), "C%d" % (C + 1), alpha=0.6, label="$C=%d$" % C)
plt.plot(xs, y_exact(xs, 2.0), "b", lw=4, alpha=0.35, label="exact, $C=2$")
plt.plot(xs[::20], ys[::20], "ro", label="Euler (C), $h=0.01$, $y(1)=1$")
plt.xlabel("$x$"); plt.ylabel("$y$"); plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq14.pdf"), bbox_inches="tight")
