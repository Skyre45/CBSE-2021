# At least one of two independent solvers succeeds: Z-transform (analysis) against the C simulation
import os
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")

pA, pB = 1 / 3, 1 / 5
pmfA = np.array([1 - pA, pA])                           # coefficients of P_A(z)
pmfB = np.array([1 - pB, pB])
pmfS = np.convolve(pmfA, pmfB)                          # coefficients of P_A(z) P_B(z)
print("PMF of S :", pmfS, "(= [8/15, 6/15, 1/15])")
print("P(S>=1) =", pmfS[1:].sum(), " 7/15 =", 7 / 15)

sim = np.loadtxt(os.path.join(DIR, "cbXIIq1.dat"))      # columns: n, relative frequency from the C program
n = sim[:, 0].astype(int)
print("simulation:", sim[:, 1], " P(S>=1) ~", sim[1:, 1].sum())

plt.stem(n, sim[:, 1], markerfmt="o", linefmt="C0-", label="Simulation (C)")
plt.stem(n, pmfS, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(n); plt.xlabel("$n$ (number of solvers who succeed)"); plt.ylabel("$p_S(n)$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq1.pdf"), bbox_inches="tight")
