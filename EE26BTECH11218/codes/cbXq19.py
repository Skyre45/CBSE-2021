# Grouped data: modal class, mode (histogram construction), median (ogive)
# Helper functions adapted from {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from cbfuncs import line_intersect, norm_vec
from cbfuncs import label_pts

edges = np.array([0, 20, 40, 60, 80, 100.0])
f = np.array([1, 4, 3, 7, 5.0])
h = edges[1] - edges[0]
N = f.sum()

# (i), (iii), (iv): modal class and median class
j = np.argmax(f)
print("modal class  :", edges[j], "-", edges[j + 1], " class mark =", 0.5 * (edges[j] + edges[j + 1]))
cf = np.cumsum(f)
k = np.argmax(cf >= N / 2)
print("median class :", edges[k], "-", edges[k + 1])
print("sum of lower limits =", edges[j] + edges[k])

# (ii) mode: intersection of the two lines drawn on the histogram
l = edges[j]
f0, f1, f2 = f[j - 1], f[j], f[j + 1]
A1, B1 = np.array([[l], [f0]]), np.array([[l + h], [f1]])        # top-right corners (preceding, modal)
A2, B2 = np.array([[l], [f1]]), np.array([[l + h], [f2]])        # top-left corners (modal, succeeding)
n1, n2 = norm_vec(A1, B1), norm_vec(A2, B2)
X = line_intersect(n1, A1, n2, A2)
print("mode (line intersection) =", X[0, 0])
print("mode (formula)           =", l + (f1 - f0) / (2 * f1 - f0 - f2) * h)

# (v) median: solve F(x) = N/2 on the piecewise-linear ogive
xs = edges
Fs = np.concatenate(([0], cf))
F = lambda x: np.interp(x, xs, Fs) - N / 2
med = brentq(F, 0, 100)
print("median (brentq on ogive) =", med)
print("median (formula)         =", edges[k] + (N / 2 - cf[k - 1]) / f[k] * h)

# plotting
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))
ax[0].bar(edges[:-1], f, width=h, align="edge", edgecolor="k", alpha=0.5)
ax[0].plot([A1[0, 0], B1[0, 0]], [A1[1, 0], B1[1, 0]], "r")
ax[0].plot([A2[0, 0], B2[0, 0]], [A2[1, 0], B2[1, 0]], "g")
ax[0].plot([X[0, 0]] * 2, [0, X[1, 0]], "k--")
ax[0].scatter(X[0, :], X[1, :], color="k", zorder=5)
label_pts(X, [f"({X[0,0]:.2f}, {X[1,0]:.2f})"])
ax[0].set_xlabel("Time (s)"); ax[0].set_ylabel("Number of students")
ax[0].set_title("Histogram: mode"); ax[0].grid(True, linestyle="--", alpha=0.6)

ax[1].plot(xs, Fs, "o-")
ax[1].axhline(N / 2, color="r", ls="--")
ax[1].plot([med, med], [0, N / 2], "k--")
M = np.array([[med], [N / 2]])
ax[1].scatter(M[0, :], M[1, :], color="k", zorder=5)
label_pts(M, [f"({med:.2f}, {N/2:.0f})"])
ax[1].set_xlabel("Time (s)"); ax[1].set_ylabel("Cumulative frequency")
ax[1].set_title("Ogive: median"); ax[1].grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "cbXq19.pdf"), bbox_inches="tight")
