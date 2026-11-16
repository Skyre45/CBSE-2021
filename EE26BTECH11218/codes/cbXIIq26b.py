# Number of sixes in two tosses of a die: binomial PMF (and its Z-transform) against the C simulation
import os
from math import comb
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")

n, p = 2, 1 / 6
k = np.arange(n + 1)
pmf = np.array([comb(n, j) * p ** j * (1 - p) ** (n - j) for j in k])
conv = np.convolve([1 - p, p], [1 - p, p])               # coefficients of (1 - p + p z^-1)^2
print("binomial PMF   :", pmf, " = [25/36, 10/36, 1/36] =", np.array([25, 10, 1]) / 36)
print("convolution    :", conv)
print("mean, variance :", (k * pmf).sum(), n * p, ((k - n * p) ** 2 * pmf).sum(), n * p * (1 - p))

sim = np.loadtxt(os.path.join(DIR, "cbXIIq26b.dat"))
print("simulation     :", sim[:, 1])

plt.stem(k, sim[:, 1], markerfmt="o", linefmt="C0-", label="Simulation (C)")
plt.stem(k, pmf, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(k); plt.xlabel("$k$ (number of successes)"); plt.ylabel("$p_X(k)$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq26b.pdf"), bbox_inches="tight")
