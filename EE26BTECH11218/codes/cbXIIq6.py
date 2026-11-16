# Improper integral of tan(arcsin x) on [0,1]: plot, with the results of the C trapezoidal-rule program
import os
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")
f = lambda x: x / np.sqrt(1 - x ** 2)                   # tan(arcsin x)

res = np.loadtxt(os.path.join(DIR, "cbXIIq6.dat"))     # columns: b, trapezoid A_n, 1 - sqrt(1-b^2)
for b, A, ex in res:
    print("b = %-6g trapezoid = %.6f   1 - sqrt(1-b^2) = %.6f" % (b, A, ex))

x = np.linspace(0, 0.999, 1000)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(x, f(x), "b"); ax[0].fill_between(x, f(x), alpha=0.3)
ax[0].set_ylim(0, 15); ax[0].set_xlabel("$x$"); ax[0].set_ylabel(r"$\tan(\sin^{-1}x)$")
ax[0].set_title("Integrand blows up at $x=1$"); ax[0].grid(True, linestyle="--", alpha=0.6)
ax[1].plot(x, 1 - np.sqrt(1 - x ** 2), "r", label=r"$1-\sqrt{1-b^2}$")
ax[1].plot(res[:, 0], res[:, 1], "ko", label="trapezoidal rule (C)")
ax[1].axhline(1, color="k", ls="--")
ax[1].set_xlabel("$b$"); ax[1].set_ylabel(r"$\int_0^b \frac{x}{\sqrt{1-x^2}}\,dx$")
ax[1].set_title("Partial integrals tend to 1"); ax[1].legend(loc="lower right"); ax[1].grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "cbXIIq6.pdf"), bbox_inches="tight")
