# Improper integral of tan(arcsin x) on [0,1]
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from scipy.integrate import quad

f = lambda x: x / np.sqrt(1 - x ** 2)            # tan(arcsin x)
val, err = quad(f, 0, 1)
print("quad            :", val, "+/-", err)
th, _ = quad(np.sin, 0, np.pi / 2)               # substitution x = sin(theta)
print("theta-substit.  :", th)
for b in [0.9, 0.99, 0.999, 0.999999]:
    print("b = %-9g int_0^b = %.6f   1-sqrt(1-b^2) = %.6f" % (b, quad(f, 0, b)[0], 1 - np.sqrt(1 - b ** 2)))

x = np.linspace(0, 0.999, 1000)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(x, f(x), "b"); ax[0].fill_between(x, f(x), alpha=0.3)
ax[0].set_ylim(0, 15); ax[0].set_xlabel("$x$"); ax[0].set_ylabel(r"$\tan(\sin^{-1}x)$")
ax[0].set_title("Integrand blows up at $x=1$"); ax[0].grid(True, linestyle="--", alpha=0.6)
ax[1].plot(x, 1 - np.sqrt(1 - x ** 2), "r"); ax[1].axhline(1, color="k", ls="--")
ax[1].set_xlabel("$b$"); ax[1].set_ylabel(r"$\int_0^b$")
ax[1].set_title("Partial integrals tend to 1"); ax[1].grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "cbXIIq6.pdf"), bbox_inches="tight")
