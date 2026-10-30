# Chord of the larger concentric circle touching the smaller one
# Helper functions adapted from {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
import os
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from cbfuncs import line_gen
from cbfuncs import circ_gen, chord
from cbfuncs import label_pts

V = np.eye(2)
u = np.zeros((2, 1))
f_big, f_small = -100.0, -36.0               # f = ||c||^2 - r^2 with c = 0
h = np.array([6.0, 0.0]).reshape(-1, 1)      # foot of the perpendicular from O onto the line
m = np.array([0.0, 1.0]).reshape(-1, 1)      # direction of the line, m^T h = 0

# tangency to the small circle: discriminant of the quadratic in kappa
g_small = (h.T @ V @ h + 2 * u.T @ h + f_small).item()
disc = (m.T @ (V @ h + u)).item() ** 2 - g_small * (m.T @ V @ m).item()
print("discriminant (small circle) =", disc)   # 0 -> tangent

# intersection with the large circle
X = chord(V, u, f_big, m, h)                  # columns are the end points
print("end points:\n", X)
print("chord length =", LA.norm(X[:, [0]] - X[:, [1]]))

# plotting
O = np.zeros((2, 1))
c1, c2 = circ_gen(O, 10), circ_gen(O, 6)
plt.figure(figsize=(6, 6))
plt.plot(c1[0, :], c1[1, :], "b", label="$r_1=10$")
plt.plot(c2[0, :], c2[1, :], "orange", label="$r_2=6$")
xc = line_gen(X[:, [0]], X[:, [1]])
plt.plot(xc[0, :], xc[1, :], "g", label="Chord $AB$")
pts = np.block([[X, h, O]])
plt.scatter(pts[0, :], pts[1, :], color="red", zorder=5)
label_pts(pts, ["$A(6,-8)$", "$B(6,8)$", "$T(6,0)$", "$O$"])
plt.xlabel("$x$"); plt.ylabel("$y$")
plt.axis("equal"); plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper left")
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs", "cbXq7.pdf"), bbox_inches="tight")
