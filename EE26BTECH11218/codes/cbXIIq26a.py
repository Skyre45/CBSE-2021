# Number of even tickets in two draws without replacement from 1..19: hypergeometric PMF
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from fractions import Fraction
from math import comb
from scipy.stats import hypergeom

M, K, n = 19, 9, 2                                # tickets, even tickets, draws
k = np.arange(n + 1)
pmf = hypergeom.pmf(k, M, K, n)
exact = [Fraction(comb(K, j) * comb(M - K, n - j), comb(M, n)) for j in k]
print("PMF    :", pmf)
print("exact  :", exact)
print("mean   :", (k * pmf).sum(), " nK/M =", n * K / M)

rng = np.random.default_rng(0)
simlen = 200000
idx = rng.random((simlen, M)).argsort(axis=1)[:, :n] + 1    # ticket numbers drawn
sim = np.bincount((idx % 2 == 0).sum(axis=1), minlength=n + 1) / simlen
print("simulation:", sim)

plt.stem(k, sim, markerfmt="o", linefmt="C0-", label="Simulation")
plt.stem(k, pmf, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(k); plt.xlabel("$k$ (even numbers)"); plt.ylabel("$p_X(k)$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq26a.pdf"), bbox_inches="tight")
