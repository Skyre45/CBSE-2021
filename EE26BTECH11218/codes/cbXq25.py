# Incircle of the right triangle ABC (B = 90 deg, AB = 8, BC = 6)
# Helper functions adapted from {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from cbfuncs import line_gen, norm_vec, perp_foot
from cbfuncs import circ_gen
from cbfuncs import tri_sides, icircle
from cbfuncs import label_pts

A = np.array([0.0, 8.0]).reshape(-1, 1)
B = np.array([0.0, 0.0]).reshape(-1, 1)
C = np.array([6.0, 0.0]).reshape(-1, 1)
c, a, b = tri_sides(A, B, C)                       # AB, BC, CA
print("sides AB, BC, CA =", c, a, b)

# (1) incentre as a weighted mean of the vertices
I1 = (a * A + b * B + c * C) / (a + b + c)
# (2) r = area / semi-perimeter
area = 0.5 * abs(np.linalg.det(np.block([C - B, A - B])))
r2 = area / (0.5 * (a + b + c))
# (3) library routine (equal-distance construction)
I3, r3 = icircle(A, B, C)
print("I (weighted mean) =", I1.ravel(), " I (icircle) =", I3.ravel())
print("r = Delta/s =", r2, " r (icircle) =", abs(r3.item()))

# (4) linear system n_i^T x - r = c_i for unknowns (x, y, r), inward unit normals
M = np.array([[1.0, 0.0, -1.0],
              [0.0, 1.0, -1.0],
              [-0.8, -0.6, -1.0]])
d = np.array([0.0, 0.0, -4.8])
sol = LA.solve(M, d)
print("(x, y, r) =", sol)

# points of contact: feet of the perpendiculars from I on the sides
nAB, nBC = np.array([[1.0], [0.0]]), np.array([[0.0], [1.0]])
nCA = np.array([[0.8], [0.6]])
P = perp_foot(nAB, 0.0, I1)
Q = perp_foot(nBC, 0.0, I1)
R = perp_foot(nCA, 4.8, I1)
print("P, Q, R =", P.ravel(), Q.ravel(), R.ravel())

# plotting
xAB, xBC, xCA = line_gen(A, B), line_gen(B, C), line_gen(C, A)
xc = circ_gen(I1, r2)
plt.figure(figsize=(6, 6))
for xl in (xAB, xBC, xCA):
    plt.plot(xl[0, :], xl[1, :], "k")
plt.plot(xc[0, :], xc[1, :], "b")
pts = np.block([[A, B, C, P, Q, R, I1]])
plt.scatter(pts[0, :], pts[1, :], color="red", zorder=5)
label_pts(pts, ["$A(0,8)$", "$B(0,0)$", "$C(6,0)$", "$P$", "$Q$", "$R$", "$O(2,2)$"])
plt.xlabel("$x$"); plt.ylabel("$y$")
plt.axis("equal"); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXq25.pdf"), bbox_inches="tight")
