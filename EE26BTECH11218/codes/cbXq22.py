# x + 2y = 5, 3x + ky + 15 = 0 has no solution: rank condition
# Helper functions adapted from {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from cbfuncs import label_pts

def system(k):
    A = np.array([[1.0, 2.0], [3.0, k]])
    b = np.array([[5.0], [-15.0]])
    return A, b

# singular A  <=>  det A(k) = k - 6 = 0
k0 = brentq(lambda k: LA.det(system(k)[0]), 0, 10)
print("k making A singular =", k0)

for k in [4.0, k0, 8.0]:
    A, b = system(k)
    rA, rAb = LA.matrix_rank(A), LA.matrix_rank(np.block([A, b]))
    status = "unique solution" if rA == 2 else ("no solution" if rA < rAb else "infinitely many")
    print(f"k = {k:.1f}: rank A = {rA}, rank [A|b] = {rAb} -> {status}")

# row reduction R2 -> R2 - 3 R1 at k = 6
A, b = system(6.0)
aug = np.block([A, b]); aug[1] = aug[1] - 3 * aug[0]
print("echelon form of [A|b] at k=6:\n", aug)

# plotting the two (parallel) lines
x = np.linspace(-6, 6, 400)
y1 = (5.0 - x) / 2.0
y2 = (-15.0 - 3.0 * x) / 6.0
plt.figure(figsize=(6, 5))
plt.plot(x, y1, "b", lw=2, label=r"$x+2y=5$")
plt.plot(x, y2, "r", lw=2, label=r"$3x+6y+15=0$")
pts = np.array([[5.0, 0.0, -5.0, 0.0], [0.0, 2.5, 0.0, -2.5]])
plt.scatter(pts[0, :], pts[1, :], color="k", zorder=5)
label_pts(pts, ["$(5,0)$", "$(0,2.5)$", "$(-5,0)$", "$(0,-2.5)$"])
plt.axhline(0, color="k", lw=0.8); plt.axvline(0, color="k", lw=0.8)
plt.ylim(-6, 6)
plt.xlabel("$x$"); plt.ylabel("$y$"); plt.title("Parallel lines: no solution ($k=6$)")
plt.grid(True, linestyle="--", alpha=0.6); plt.legend(loc="upper right")
plt.savefig(os.path.join(FIG, "cbXq22.pdf"), bbox_inches="tight")
