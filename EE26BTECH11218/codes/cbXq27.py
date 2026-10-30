# Polynomial division f(x) = q(x) g(x) + r(x) as a linear system, and the remainder theorem over C
import os
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
f = np.array([5.0, 10.0, -30.0, -15.0])      # 5x^3 + 10x^2 - 30x - 15
g = np.array([1.0, 1.0, 1.0])                # x^2 + x + 1

# (1) library long division
q, r = np.polydiv(f, g)
print("polydiv: q =", q, " r =", r)

# (2) matrix equation: f = conv(g, q) + [0, 0, r1, r0] with unknowns (q1, q0, r1, r0)
M = np.array([[1, 0, 0, 0],
              [1, 1, 0, 0],
              [1, 1, 1, 0],
              [0, 1, 0, 1]], dtype=float)
sol = LA.solve(M, f)
print("(q1, q0, r1, r0) =", sol)

# (3) remainder theorem: r(w) = f(w) at the complex roots w of g
w = np.roots(g)
print("roots of g:", w)
fw = np.polyval(f, w)
# r(x) = r1 x + r0 passes through (w_i, f(w_i)):  [[w1, 1],[w2, 1]] (r1, r0)^T = f(w)
Rm = np.array([[w[0], 1], [w[1], 1]])
print("(r1, r0) from roots =", np.round(LA.solve(Rm, fw), 10))

# plotting
x = np.linspace(-4, 4, 400)
plt.figure(figsize=(6.5, 4.5))
plt.plot(x, np.polyval(f, x), "b", lw=2.5, label=r"$f(x)$")
plt.plot(x, np.polyval(np.polymul(q, g), x), "r--", lw=1.5, label=r"$q(x)g(x)$")
plt.plot(x, np.polyval(r, x), "g", label=r"$r(x)=-40x-20$")
plt.plot(x, np.polyval(np.polyadd(np.polymul(q, g), r), x), "k:", lw=2, label=r"$q(x)g(x)+r(x)$")
plt.ylim(-300, 300)
plt.xlabel("$x$"); plt.ylabel("$y$"); plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper left")
plt.savefig(os.path.join(FIG, "cbXq27.pdf"), bbox_inches="tight")
