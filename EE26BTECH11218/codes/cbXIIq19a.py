# Symmetric matrix [[4, x+2],[2x-3, x+1]]: the skew-symmetric part must vanish
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy.linalg as LA
from scipy.optimize import brentq

A = lambda x: np.array([[4.0, x + 2], [2 * x - 3, x + 1]])
S = lambda x: 0.5 * (A(x) + A(x).T)                 # symmetric part
K = lambda x: 0.5 * (A(x) - A(x).T)                 # skew-symmetric part, = (5-x)/2 [[0,1],[-1,0]]

x0 = brentq(lambda x: K(x)[0, 1], -10, 10)
print("x =", x0)
print("A(x) =\n", A(x0), "\nsymmetric:", np.allclose(A(x0), A(x0).T))
print("K(0) =\n", K(0.0))

x = np.linspace(-2, 12, 200)
nK = np.array([LA.norm(K(t), "fro") for t in x])
plt.plot(x, nK, "b")
plt.scatter([x0], [0], color="red", zorder=5)
plt.annotate("$x=5$", (x0, 0), textcoords="offset points", xytext=(8, 8))
plt.xlabel("$x$"); plt.ylabel(r"$\|K(x)\|_F$"); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq19a.pdf"), bbox_inches="tight")
