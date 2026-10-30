# Number of outcomes when three dice are thrown: 6^3 via convolution of PMFs
# Adapted from {https://github.com/gadepall/probability} (codes/sum/dice.py)
import os
import numpy as np
import matplotlib.pyplot as plt

# one die: count of outcomes for each face 1..6 (indices 1..6, index 0 unused)
die = np.array([0, 1, 1, 1, 1, 1, 1])

# (x + x^2 + ... + x^6)^3  <->  repeated convolution
two = np.convolve(die, die)
three = np.convolve(two, die)                  # index n = number of outcomes with sum n
n = np.arange(len(three))
print("total outcomes =", three.sum(), " 6^3 =", 6 ** 3)

# simulation: draw many triples and count the distinct ones seen
rng = np.random.default_rng(0)
y = rng.integers(1, 7, size=(3, 200000))
code = (y[0] - 1) * 36 + (y[1] - 1) * 6 + (y[2] - 1)
print("distinct triples seen =", np.unique(code).size)

# simulated count of sums scaled to the 216-outcome space
sums = y.sum(axis=0)
counts = np.bincount(sums, minlength=len(three)) / y.shape[1] * 216

# plotting
idx = np.arange(3, 19)
plt.stem(idx, counts[idx], markerfmt="o", linefmt="C0-", label="Simulation (scaled)")
plt.stem(idx + 0.0, three[idx], markerfmt="x", linefmt="C3--", label="Analysis")
plt.xlabel("$n$ (sum of the three dice)")
plt.ylabel("Number of outcomes with sum $n$")
plt.title(r"$\sum_n$ (outcomes) $=216$")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs", "cbXq16.pdf"), bbox_inches="tight")
