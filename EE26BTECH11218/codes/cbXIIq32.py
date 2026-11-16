# Two red balls drawn: which bag?  Bayes' theorem with hypergeometric likelihoods against the C simulation
import os
from math import comb
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")

# B = bag chosen (1 or 2), p_B(1) = p_B(2) = 1/2;  bag 1: 5R 4B,  bag 2: 3R 6B
# X = number of red balls among the two drawn;  the data is the event {X = 2}
prior = np.array([0.5, 0.5])
lik = np.array([comb(5, 2) / comb(9, 2), comb(3, 2) / comb(9, 2)])      # p_{X|B}(2 | b)
post = prior * lik / (prior * lik).sum()
print("likelihoods:", lik, " = [10/36, 3/36]")
print("posterior  :", post, " P(B=2 | X=2) =", post[1], " 3/13 =", 3 / 13)

sim = np.loadtxt(os.path.join(DIR, "cbXIIq32.dat"))     # columns: b, estimate of P(B=b | X=2) from the C program
b = sim[:, 0].astype(int)
print("simulation :", sim[:, 1])

plt.stem(b, sim[:, 1], markerfmt="o", linefmt="C0-", label="Simulation (C)")
plt.stem(b, post, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(b, ["bag 1 (5R,4B)", "bag 2 (3R,6B)"]); plt.ylabel(r"$P(B=b\mid X=2)$")
plt.xlim(0.5, 2.5); plt.ylim(0, 1)
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq32.pdf"), bbox_inches="tight")
