# x y' - y = log x : integrating factor and solution (numerical check with solve_ivp)
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from scipy.integrate import solve_ivp

mu = lambda x: 1 / x                              # integrating factor
y_exact = lambda x, C: -np.log(x) - 1 + C * x     # (y/x)' = log(x)/x^2

rhs = lambda x, y: (y + np.log(x)) / x
xs = np.linspace(1, 5, 200)
sol = solve_ivp(rhs, (1, 5), [1.0], t_eval=xs, rtol=1e-10, atol=1e-12)    # y(1)=1 -> C=2
print("max |numerical - exact| =", np.max(np.abs(sol.y[0] - y_exact(xs, 2.0))))

# check that (mu*y)' = log(x)/x^2
x0, h = 2.0, 1e-6
d = (mu(x0 + h) * y_exact(x0 + h, 2.0) - mu(x0 - h) * y_exact(x0 - h, 2.0)) / (2 * h)
print("(mu y)' =", d, "  log(x)/x^2 =", np.log(x0) / x0 ** 2)

for C in [0, 1, 3]:
    plt.plot(xs, y_exact(xs, C), "C%d" % (C + 1), alpha=0.6, label="$C=%d$" % C)
plt.plot(xs, y_exact(xs, 2.0), "b", lw=4, alpha=0.35, label="exact, $C=2$")
plt.plot(xs[::10], sol.y[0][::10], "ro", label="numerical, $y(1)=1$")
plt.xlabel("$x$"); plt.ylabel("$y$"); plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq14.pdf"), bbox_inches="tight")
