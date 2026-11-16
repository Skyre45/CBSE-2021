# Three cards from a deck of 52, no replacement: hypergeometric PMF against the C simulation
import os
from math import comb
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")

k = np.arange(4)
pmf = np.array([comb(26, j) * comb(26, 3 - j) / comb(52, 3) for j in k])   # p_X(k)
print("PMF:", pmf, " p_X(2) =", pmf[2], " 13/34 =", 13 / 34)

sim = np.loadtxt(os.path.join(DIR, "cbXIIq15.dat"))
print("simulation:", sim[:, 1])

plt.stem(k, sim[:, 1], markerfmt="o", linefmt="C0-", label="Simulation (C)")
plt.stem(k, pmf, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(k); plt.xlabel("$k$ (red cards)"); plt.ylabel("$p_X(k)$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq15.pdf"), bbox_inches="tight")
