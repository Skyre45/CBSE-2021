# Number of even tickets in two draws without replacement from 1..19: hypergeometric PMF against the C simulation
import os
from math import comb
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")

k = np.arange(3)
pmf = np.array([comb(9, j) * comb(10, 2 - j) / comb(19, 2) for j in k])    # p_X(k)
print("PMF    :", pmf, " = [5/19, 10/19, 4/19] =", np.array([5, 10, 4]) / 19)
print("mean   :", (k * pmf).sum(), " 18/19 =", 18 / 19)

sim = np.loadtxt(os.path.join(DIR, "cbXIIq26a.dat"))
print("simulation:", sim[:, 1])

plt.stem(k, sim[:, 1], markerfmt="o", linefmt="C0-", label="Simulation (C)")
plt.stem(k, pmf, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(k); plt.xlabel("$k$ (even numbers)"); plt.ylabel("$p_X(k)$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq26a.pdf"), bbox_inches="tight")
