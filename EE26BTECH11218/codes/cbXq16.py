# Number of outcomes when three dice are thrown: Z-transform of the dice (analysis) against the C simulation
import os
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")

# one die: x(n) = 1 for n = 1..6 (index 0 unused);  X(z) = z^-1 + ... + z^-6
die = np.array([0, 1, 1, 1, 1, 1, 1])
three = np.convolve(np.convolve(die, die), die)         # coefficients of X(z)^3: index n = outcomes with sum n
print("total outcomes =", three.sum(), " 6^3 =", 6 ** 3)

sim = np.loadtxt(os.path.join(DIR, "cbXq16.dat"))       # columns: n, scaled frequency from the C program
n = sim[:, 0].astype(int)

plt.stem(n, sim[:, 1], markerfmt="o", linefmt="C0-", label="Simulation (C)")
plt.stem(n, three[n], markerfmt="x", linefmt="C3--", label="Analysis")
plt.xlabel("$n$ (sum of the three dice)")
plt.ylabel("Number of outcomes with sum $n$")
plt.title(r"$\sum_n$ (outcomes) $=216$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXq16.pdf"), bbox_inches="tight")
