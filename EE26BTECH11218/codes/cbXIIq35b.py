# Partial fractions of x / ((x-1)^2 (x+2)) and its antiderivative
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy.linalg as LA
from scipy.integrate import quad
from scipy.signal import residue

# x = A(x-1)(x+2) + B(x+2) + C(x-1)^2   -> match the coefficients of x^2, x, 1
M = np.array([[1.0, 0.0, 1.0],
              [1.0, 1.0, -2.0],
              [-2.0, 2.0, 1.0]])
rhs = np.array([0.0, 1.0, 0.0])
A_, B_, C_ = LA.solve(M, rhs)
print("A, B, C =", A_, B_, C_, " (2/9, 1/3, -2/9)")
r, p, k = residue([1, 0], np.poly([1, 1, -2]))
print("scipy.signal.residue:", np.round(r, 4), np.round(p, 4))

f = lambda x: x / ((x - 1) ** 2 * (x + 2))
F = lambda x: 2 / 9 * np.log(np.abs(x - 1)) - 1 / (3 * (x - 1)) - 2 / 9 * np.log(np.abs(x + 2))
print("partial fractions agree:", np.allclose(f(3.7), A_ / 2.7 + B_ / 2.7 ** 2 + C_ / 5.7))
print("int_2^5 f dx (quad) =", quad(f, 2, 5)[0], "  F(5)-F(2) =", F(5) - F(2))
h, x0 = 1e-6, 3.0
print("F'(3) =", (F(x0 + h) - F(x0 - h)) / (2 * h), "  f(3) =", f(x0))

x = np.linspace(1.2, 5, 300)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(x, f(x), "b", label="$f(x)$")
ax[0].plot(x, A_ / (x - 1), "--", label="$A/(x-1)$")
ax[0].plot(x, B_ / (x - 1) ** 2, "--", label="$B/(x-1)^2$")
ax[0].plot(x, C_ / (x + 2), "--", label="$C/(x+2)$")
ax[0].set_ylim(-0.5, 1.5); ax[0].legend(); ax[0].set_title("Partial fractions")
ax[1].plot(x, F(x), "r"); ax[1].set_title("Antiderivative $F(x)$")
for a_ in ax:
    a_.set_xlabel("$x$"); a_.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "cbXIIq35b.pdf"), bbox_inches="tight")
