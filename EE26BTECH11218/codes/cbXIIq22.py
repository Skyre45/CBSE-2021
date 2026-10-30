# A adj(A) = adj(A) A = |A| I  via Cayley-Hamilton
# Adapted from {https://github.com/gadepall/matgeo/tree/main/codes/book/cayley.py}
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy.linalg as LA
from cbfuncs import polyvalm

A = np.array([[2.0, 3.0], [-4.0, -6.0]])
t, d = np.trace(A), LA.det(A)
print("tr A =", t, " |A| =", d)
print("Cayley-Hamilton  A^2 - tr(A) A + |A| I =\n", polyvalm(np.poly(A), A))

adj_CH = t * np.eye(2) - A                         # follows from Cayley-Hamilton for 2x2

def adjugate(A):                                   # transpose of the cofactor matrix
    n = A.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            C[i, j] = (-1) ** (i + j) * LA.det(minor)
    return C.T

adj = adjugate(A)
print("adj A =\n", adj, "\nsame as tr(A)I - A:", np.allclose(adj, adj_CH))
print("A adj A =\n", np.round(A @ adj, 10), "\nadj A A =\n", np.round(adj @ A, 10), "\n|A| I =\n", np.round(d * np.eye(2), 10))
print("identity holds:", np.allclose(A @ adj, d * np.eye(2)) and np.allclose(adj @ A, d * np.eye(2)))

th = np.linspace(0, 2 * np.pi, 200)
U = np.vstack((np.cos(th), np.sin(th)))
fig = plt.figure(figsize=(6, 6))
plt.plot(U[0], U[1], "k", label="unit circle")
imA, imadj = A @ U, adj @ U
plt.plot(imA[0], imA[1], "b", lw=3, label="image under $A$")
plt.plot(imadj[0], imadj[1], "r", lw=3, label="image under adj $A$")
s = np.linspace(-2.2, 2.2, 2)
plt.plot(3 * s, -2 * s, "g--", label="null space of $A$")
plt.axis("equal")
plt.xlabel("$x$"); plt.ylabel("$y$"); plt.grid(True, linestyle="--", alpha=0.6); plt.legend(loc="upper left")
plt.savefig(os.path.join(FIG, "cbXIIq22.pdf"), bbox_inches="tight")
