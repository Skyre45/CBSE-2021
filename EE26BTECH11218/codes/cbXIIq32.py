# Two red balls drawn: which bag did they come from?  Bayes' theorem with hypergeometric likelihoods
# Adapted from {https://github.com/gadepall/probability}
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from fractions import Fraction
from scipy.stats import hypergeom

prior = np.array([0.5, 0.5])                        # bag 1: 5R 4B,  bag 2: 3R 6B
lik = np.array([hypergeom.pmf(2, 9, 5, 2), hypergeom.pmf(2, 9, 3, 2)])     # P(RR | bag)
post = prior * lik / (prior * lik).sum()
print("likelihoods:", lik, " = [10/36, 3/36] =", np.array([10, 3]) / 36)
print("posterior  :", post, " P(bag 2 | RR) =", post[1], " 3/13 =", Fraction(3, 13), "=", 3 / 13)

# simulation: sequential draws without replacement, keep trials with two reds
rng = np.random.default_rng(0)
N = 2 * 10 ** 6
bag = rng.integers(0, 2, N)
R = np.where(bag == 0, 5, 3)
first = rng.random(N) < R / 9
second = rng.random(N) < np.where(first, R - 1, R) / 8
both = first & second
print("simulation: P(bag 2 | RR) =", np.mean(bag[both] == 1))

x = np.arange(2)
plt.bar(x - 0.18, prior, 0.36, label="prior $P(B_i)$")
plt.bar(x + 0.18, post, 0.36, label="posterior $P(B_i\\mid RR)$")
plt.xticks(x, ["bag 1 (5R,4B)", "bag 2 (3R,6B)"]); plt.ylabel("probability")
plt.legend(); plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq32.pdf"), bbox_inches="tight")
