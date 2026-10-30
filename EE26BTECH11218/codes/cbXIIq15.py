# Three cards from a deck of 52, no replacement: hypergeometric PMF
# Adapted from {https://github.com/gadepall/probability} (binomial/binomial.py)
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from math import comb
from fractions import Fraction
from scipy.stats import hypergeom

M, K, n = 52, 26, 3                               # deck, red cards, draws
k = np.arange(n + 1)
pmf = hypergeom.pmf(k, M, K, n)
print("PMF:", pmf)
print("P(2 red, 1 black) =", pmf[2], " C(26,2)C(26,1)/C(52,3) =", Fraction(comb(26, 2) * comb(26, 1), comb(52, 3)))

rng = np.random.default_rng(0)
deck = np.array([1] * K + [0] * (M - K))
simlen = 100000
idx = rng.random((simlen, M)).argsort(axis=1)[:, :n]      # n cards without replacement
sim = np.bincount(deck[idx].sum(axis=1), minlength=n + 1) / simlen
print("simulation:", sim)

plt.stem(k, sim, markerfmt="o", linefmt="C0-", label="Simulation")
plt.stem(k, pmf, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(k); plt.xlabel("$k$ (red cards)"); plt.ylabel("$p_K(k)$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq15.pdf"), bbox_inches="tight")
