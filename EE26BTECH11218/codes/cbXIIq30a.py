# Shortest distance between skew lines by least squares
# Adapted from {https://github.com/gadepall/matgeo/tree/main/codes/book/skew_least.py}
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy.linalg as LA
from cbfuncs import line_gen_num

P1 = np.array([1.0, -1.0, 0.0]).reshape(-1, 1)     # L1: (x-1)/2 = (y+1)/3 = z
m1 = np.array([2.0, 3.0, 1.0]).reshape(-1, 1)
P2 = np.array([-1.0, 2.0, 2.0]).reshape(-1, 1)     # L2: (x+1)/5 = y-2, z = 2
m2 = np.array([5.0, 1.0, 0.0]).reshape(-1, 1)

b = P2 - P1
M = np.block([m1, m2])
x, res, rank, sv = LA.lstsq(M, b, rcond=None)      # minimise ||M x - b||,  x = (s, -t)
d_ls = LA.norm(M @ x - b)
n = np.cross(m1.ravel(), m2.ravel())
d_cross = abs(b.ravel() @ n) / LA.norm(n)
print("m1 x m2 =", n, " (b.n) =", b.ravel() @ n)
print("(s, -t) =", x.ravel(), " normal equations:", LA.solve(M.T @ M, M.T @ b).ravel())
print("distance (least squares) =", d_ls, " (triple product) =", d_cross, " 9/sqrt(195) =", 9 / np.sqrt(195))
print("lines intersect:", bool(d_ls < 1e-9))

Q1 = P1 + x[0, 0] * m1                              # closest points
Q2 = P2 - x[1, 0] * m2
print("closest points:", Q1.ravel(), Q2.ravel())

x1 = line_gen_num(P1 - 2 * m1, P1 + 3 * m1, 50)
x2 = line_gen_num(P2 - 1 * m2, P2 + 1 * m2, 50)
xp = line_gen_num(Q1, Q2, 10)
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d")
ax.plot(x1[0], x1[1], x1[2], "b", label="$L_1$")
ax.plot(x2[0], x2[1], x2[2], "r", label="$L_2$")
ax.plot(xp[0], xp[1], xp[2], "g", lw=3, label="common perpendicular")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$"); ax.legend()
plt.savefig(os.path.join(FIG, "cbXIIq30a.pdf"), bbox_inches="tight")
