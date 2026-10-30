# Tangent-radius orthogonality and the isosceles triangle OPQ
# Helper functions adapted from {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
# Run from the project root:  python codes/cbq6/cbq6.py
import os
import numpy as np
import matplotlib.pyplot as plt
from cbfuncs import line_gen, ang_vec
from cbfuncs import circ_gen
from cbfuncs import label_pts

# centre, point of contact, and Q on the tangent with ||PQ|| = ||OP||
r = 2.0
O = np.array([0.0, 0.0]).reshape(-1, 1)
P = np.array([r, 0.0]).reshape(-1, 1)
m = np.array([0.0, 1.0]).reshape(-1, 1)      # tangent direction, m^T (P-O) = 0
Q = P + r * m

print("m^T(P-O) =", (m.T @ (P - O)).item())     # tangent is perpendicular to radius
print("|OP|, |PQ|, |OQ| =", np.linalg.norm(O - P), np.linalg.norm(P - Q), np.linalg.norm(O - Q))
print("angle OPQ =", np.degrees(ang_vec(O - P, Q - P)))
print("angle OQP =", np.degrees(ang_vec(O - Q, P - Q)))   # expected 45 degrees
print("angle POQ =", np.degrees(ang_vec(P - O, Q - O)))

# plotting
x_circ = circ_gen(O, r)
x_OP = line_gen(O, P)
x_PQ = line_gen(P - r * m, Q + r * 0.5 * m)  # tangent line
x_OQ = line_gen(O, Q)

plt.figure(figsize=(6, 6))
plt.plot(x_circ[0, :], x_circ[1, :], "b", label="Circle")
plt.plot(x_OP[0, :], x_OP[1, :], "k")
plt.plot(x_PQ[0, :], x_PQ[1, :], "g", label="Tangent $PQ$")
plt.plot(x_OQ[0, :], x_OQ[1, :], "r--")
pts = np.block([[O, P, Q]])
plt.scatter(pts[0, :], pts[1, :], color="red", zorder=5)
label_pts(pts, ["$O(0,0)$", "$P(2,0)$", "$Q(2,2)$"])
plt.annotate(r"$45^\circ$", (1.5, 2.0 * 0.35 + 1.5 * 0.0), xytext=(-5, -5), textcoords="offset points")
plt.xlabel("$x$"); plt.ylabel("$y$")
plt.axis("equal"); plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper left")
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs", "cbXq6.pdf"), bbox_inches="tight")
