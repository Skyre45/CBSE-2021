# Perpendicular lines in space: L1: x=5, y/(3-a)=z/(-2);  L2: x=2, y/(-1)=z/(2-a)
# Adapted from {https://github.com/gadepall/matgeo/tree/main/codes/book/orth.py}
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from scipy.optimize import brentq
from cbfuncs import line_gen_num

m1 = lambda a: np.array([0.0, 3 - a, -2.0])      # direction of L1
m2 = lambda a: np.array([0.0, -1.0, 2 - a])      # direction of L2
f = lambda a: m1(a) @ m2(a)                      # inner product, = 3a - 7

c1 = f(1.0) - f(0.0)                             # f is linear in a
print("f(a) = %.0f a + (%.0f)" % (c1, f(0.0)))
a0 = brentq(f, -10, 10)
print("alpha =", a0, " 7/3 =", 7 / 3)
for name, a in zip("ABCD", [2 / 3, 3, 4, 7 / 3]):
    print(name, a, " m1.m2 =", f(a))
cosang = f(a0) / (np.linalg.norm(m1(a0)) * np.linalg.norm(m2(a0)))
print("angle =", np.degrees(np.arccos(cosang)))

P1, P2 = np.array([[5.0], [0], [0]]), np.array([[2.0], [0], [0]])
d1, d2 = m1(a0).reshape(-1, 1), m2(a0).reshape(-1, 1)
x1 = line_gen_num(P1 - 3 * d1, P1 + 3 * d1, 50)
x2 = line_gen_num(P2 - 3 * d2, P2 + 3 * d2, 50)
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d")
ax.plot(x1[0], x1[1], x1[2], "b", label="$L_1$")
ax.plot(x2[0], x2[1], x2[2], "r", label="$L_2$")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$"); ax.legend()
plt.savefig(os.path.join(FIG, "cbXIIq3.pdf"), bbox_inches="tight")
