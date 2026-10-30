# Case study: pair of paths 2x-3y=5 and -6x+9y=7 (rank / consistency analysis)
# Helper functions adapted from {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from cbfuncs import line_gen_num
from cbfuncs import label_pts

A = np.array([[2.0, -3.0], [-6.0, 9.0]])
b = np.array([[5.0], [7.0]])
aug = np.block([A, b])
print("det A =", LA.det(A))
print("rank A =", LA.matrix_rank(A), " rank [A|b] =", LA.matrix_rank(aug))   # 1 < 2: no solution

# (ii) which candidate point lies on 2x - 3y = 5 ?
n1 = A[0].reshape(-1, 1)
cands = {"A": (-4, 1), "B": (4, -1), "C": (4, 1), "D": (-4, -1)}
for k, v in cands.items():
    print(k, v, "n^T x =", (n1.T @ np.array(v).reshape(-1, 1)).item())

# (iii) intersection of -6x + 9y = 7 with the y-axis: x = 0
n2 = A[1].reshape(-1, 1)
y0 = 7.0 / n2[1, 0]
print("y-intercept =", y0, "= 7/9 =", 7 / 9)

# distance between the parallel lines (normalise n2 = -3 n1)
d = abs(5.0 - 7.0 / (-3.0)) / LA.norm(n1)
print("distance between the paths =", d)

# plotting
P1, P2 = np.array([[-2.0], [-3.0]]), np.array([[6.0], [7.0 / 3.0]])     # on 2x-3y=5
Q1, Q2 = np.array([[-2.0], [-5.0 / 9.0]]), np.array([[6.0], [43.0 / 9.0]])  # on -6x+9y=7
x1 = line_gen_num(P1, P2, 50)
x2 = line_gen_num(Q1, Q2, 50)
plt.figure(figsize=(6, 5))
plt.plot(x1[0, :], x1[1, :], "b", label=r"$2x-3y=5$")
plt.plot(x2[0, :], x2[1, :], "r", label=r"$-6x+9y=7$")
pts = np.array([[4.0, 0.0], [1.0, 7.0 / 9.0]])
plt.scatter(pts[0, :], pts[1, :], color="k", zorder=5)
label_pts(pts, ["$(4,1)$", "$(0,7/9)$"])
plt.axhline(0, color="k", lw=0.8); plt.axvline(0, color="k", lw=0.8)
plt.xlabel("$x$"); plt.ylabel("$y$"); plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper left")
plt.savefig(os.path.join(FIG, "cbXq17.pdf"), bbox_inches="tight")
