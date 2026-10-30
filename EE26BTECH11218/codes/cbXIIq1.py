# At least one of two independent solvers succeeds: PMF of a sum of Bernoulli variables
# Adapted from {https://github.com/gadepall/probability} (sum/dice.py, bernoulli/bernoulli.py)
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from scipy.stats import bernoulli

pA, pB = 1 / 3, 1 / 5
pmfA = np.array([1 - pA, pA])
pmfB = np.array([1 - pB, pB])

joint = np.outer(pmfA, pmfB)               # independence: p(x,y) = pA(x) pB(y)
pmfS = np.convolve(pmfA, pmfB)             # PMF of S = X_A + X_B
print("joint PMF:\n", joint)
print("PMF of S :", pmfS, "(= [8/15, 6/15, 1/15])")
print("P(S>=1) =", pmfS[1:].sum(), " 7/15 =", 7 / 15)

simlen = 10 ** 6
S = bernoulli.rvs(pA, size=simlen, random_state=0) + bernoulli.rvs(pB, size=simlen, random_state=1)
sim = np.bincount(S, minlength=3) / simlen
print("simulation:", sim, " P(S>=1) ~", sim[1:].sum())

n = np.arange(3)
plt.stem(n, sim, markerfmt="o", linefmt="C0-", label="Simulation")
plt.stem(n, pmfS, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(n); plt.xlabel("$n$ (number of solvers who succeed)"); plt.ylabel("$p_S(n)$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq1.pdf"), bbox_inches="tight")
