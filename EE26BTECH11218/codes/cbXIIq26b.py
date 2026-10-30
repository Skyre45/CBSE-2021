# Number of sixes in two tosses of a die: binomial PMF
# Adapted from {https://github.com/gadepall/probability} (binomial/binomial.py)
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from scipy.stats import binom, bernoulli

n, p = 2, 1 / 6
k = np.arange(n + 1)
pmf = binom.pmf(k, n, p)
conv = np.convolve([1 - p, p], [1 - p, p])               # sum of two Bernoulli variables
print("binomial PMF   :", pmf, " = [25/36, 10/36, 1/36] =", np.array([25, 10, 1]) / 36)
print("convolution    :", conv)
print("mean, variance :", (k * pmf).sum(), n * p, ((k - n * p) ** 2 * pmf).sum(), n * p * (1 - p))

simlen = 10 ** 6
X = bernoulli.rvs(p, size=(n, simlen), random_state=0).sum(axis=0)
sim = np.bincount(X, minlength=n + 1) / simlen
print("simulation     :", sim)

plt.stem(k, sim, markerfmt="o", linefmt="C0-", label="Simulation")
plt.stem(k, pmf, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(k); plt.xlabel("$k$ (number of successes)"); plt.ylabel("$p_X(k)$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq26b.pdf"), bbox_inches="tight")
