# Line through A(1,3), B(0,0) and triangle area using determinants
# Helper functions adapted from {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy.linalg as LA
from scipy.optimize import brentq
from cbfuncs import line_gen, label_pts

A = np.array([[1.0], [3.0]])
B = np.array([[0.0], [0.0]])

# (x, y) on line AB  <=>  det [[x,y,1],[A,1],[B,1]] = 0  (affine in x and y)
f = lambda x, y: LA.det(np.array([[x, y, 1.0], [A[0, 0], A[1, 0], 1], [B[0, 0], B[1, 0], 1]]))
a, b, c = f(1, 0) - f(0, 0), f(0, 1) - f(0, 0), f(0, 0)
print("line AB: %.0f x + (%.0f) y + %.0f = 0" % (a, b, c))

# area of triangle ABD(k, 0)
area = lambda k: 0.5 * abs(LA.det(np.array([[A[0, 0], A[1, 0], 1.0], [B[0, 0], B[1, 0], 1], [k, 0, 1]])))
print("area(k) / |k| =", area(2.0) / 2.0, "  (linear in |k|)")
k1 = brentq(lambda k: area(k) - 3, 0, 10)
k2 = brentq(lambda k: area(k) - 3, -10, 0)
print("k =", k1, k2)

x_AB = line_gen(A * -0.6, A * 2.2)
plt.figure(figsize=(6, 5))
plt.plot(x_AB[0], x_AB[1], "k", label="$3x-y=0$")
for k, col in ((k1, "C0"), (k2, "C3")):
    D = np.array([[k], [0.0]])
    T = np.block([[A, B, D, A]])
    plt.plot(T[0], T[1], col, label="$k=%.0f$" % k)
pts = np.block([[A, B, np.array([[k1], [0.0]]), np.array([[k2], [0.0]])]])
plt.scatter(pts[0], pts[1], color="red", zorder=5)
label_pts(pts, ["$A(1,3)$", "$B(0,0)$", "$D(2,0)$", "$D(-2,0)$"])
plt.xlabel("$x$"); plt.ylabel("$y$"); plt.axis("equal"); plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper left")
plt.savefig(os.path.join(FIG, "cbXIIq28b.pdf"), bbox_inches="tight")
