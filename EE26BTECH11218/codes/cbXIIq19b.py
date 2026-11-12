# A^2 = A  =>  (2I + A)^3 - 19A = 8I : polynomial division and projection matrices
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy.linalg as LA

p = np.poly1d([1, 2]) ** 3 - np.poly1d([19, 0])          # p(l) = (l+2)^3 - 19 l
print("p(l) =", p.coeffs)
q, r = np.polydiv(p.coeffs, [1, -1, 0])                  # divide by l^2 - l
print("quotient =", q, " remainder =", r)

rng = np.random.default_rng(1)
Q, _ = LA.qr(rng.standard_normal((4, 2)))
A1 = Q @ Q.T                                             # orthogonal projector
X, Y = rng.standard_normal((4, 2)), rng.standard_normal((4, 2))
A2 = X @ LA.inv(Y.T @ X) @ Y.T                           # oblique projector
I = np.eye(4)
for A in (A1, A2):
    R = np.linalg.matrix_power(2 * I + A, 3) - 19 * A
    print("A^2=A:", np.allclose(A @ A, A), " eig:", np.round(np.sort(LA.eigvals(A).real), 6),
          " (2I+A)^3-19A = 8I:", np.allclose(R, 8 * I))

l = np.linspace(-1, 2, 200)
plt.plot(l, p(l), "b")
pts = np.array([[0.0, 1.0], [8.0, 8.0]])
plt.scatter(pts[0], pts[1], color="red", zorder=5)
plt.annotate("$(0,8)$", (0, 8), textcoords="offset points", xytext=(-35, 8))
plt.annotate("$(1,8)$", (1, 8), textcoords="offset points", xytext=(5, -15))
plt.xlabel(r"$\lambda$"); plt.ylabel(r"$p(\lambda)=(2+\lambda)^3-19\lambda$")
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq19b.pdf"), bbox_inches="tight")
