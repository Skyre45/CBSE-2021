# Which antiderivative is correct?  Compare numerical integration with each option
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from scipy.integrate import quad

g = lambda x: np.exp(x) / (x + 1) * (1 + (x + 1) * np.log(x + 1))
F = {
    "A": lambda x: np.exp(x) / (x + 1),
    "B": lambda x: np.exp(x) * x / (x + 1),
    "C": lambda x: np.exp(x) * np.log(x + 1) + np.exp(x),
    "D": lambda x: np.exp(x) * np.log(x + 1),
}
print("   b    quad     " + "    ".join(F))
for b in [0.5, 1.0, 2.0]:
    I = quad(g, 0, b)[0]
    print("%4.1f  %8.5f  " % (b, I) + "  ".join("%8.5f" % (F[k](b) - F[k](0)) for k in F))

h = 1e-6
x0 = 1.3
print("dF_D/dx =", (F["D"](x0 + h) - F["D"](x0 - h)) / (2 * h), " integrand =", g(x0))

b = np.linspace(0, 3, 200)
I = np.array([quad(g, 0, t)[0] for t in b])
plt.plot(b, I, "k", lw=4, alpha=0.35, label="numerical $\\int_0^b$")
for k, st in zip(F, ["--", "-.", ":", "-"]):
    plt.plot(b, F[k](b) - F[k](0), st, label="option (%s)" % k)
plt.xlabel("$b$"); plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq7.pdf"), bbox_inches="tight")
