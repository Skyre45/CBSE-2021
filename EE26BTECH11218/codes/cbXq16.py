# Number of outcomes when three dice are thrown: 6^3 via Z-transform/convolution
import os
import numpy as np
import matplotlib.pyplot as plt

# one die: count of outcomes for each face 1..6 (indices 1..6, index 0 unused)
die = np.array([0, 1, 1, 1, 1, 1, 1])

# Z-transform product: (z^-1 + ... + z^-6)^3 computed via repeated convolution
two = np.convolve(die, die)
three = np.convolve(two, die)
n = np.arange(len(three))
print("total outcomes =", three.sum(), " 6^3 =", 6 ** 3)

rng = np.random.default_rng(0)
y = rng.integers(1, 7, size=(3, 200000))
sums = y.sum(axis=0)
counts = np.bincount(sums, minlength=len(three)) / y.shape[1] * 216

idx = np.arange(3, 19)
plt.stem(idx, counts[idx], markerfmt="o", linefmt="C0-", label="Simulation (scaled)")
plt.stem(idx + 0.0, three[idx], markerfmt="x", linefmt="C3--", label="Analysis (Z-transform)")
plt.xlabel("$n$ (sum of the three dice)")
plt.ylabel("Number of outcomes with sum $n$")
plt.title(r"$\sum_n$ (outcomes) $=216$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs", "cbXq16.pdf"), bbox_inches="tight")
