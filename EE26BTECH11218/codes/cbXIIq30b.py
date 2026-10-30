# Plane through the line of intersection of two planes at unit distance from the origin
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy.linalg as LA

n1, e1 = np.array([1.0, 3.0, 0.0]), 6.0            # x + 3y + 6 = 0
n2, e2 = np.array([3.0, -1.0, -4.0]), 0.0          # 3x - y - 4z = 0

# pencil: (n1 + l n2).x + (e1 + l e2) = 0 ; unit distance: |e| = ||n||
coef = [n2 @ n2 - e2 ** 2, 2 * (n1 @ n2 - e1 * e2), n1 @ n1 - e1 ** 2]
lam = np.roots(coef)
print("quadratic coefficients:", coef, " lambda =", lam)

planes = []
for l in sorted(lam.real):
    n, e = n1 + l * n2, e1 + l * e2
    print("lambda = %+.0f : normal %s, constant %.0f, distance from origin = %.6f" % (l, n, e, abs(e) / LA.norm(n)))
    planes.append((n, e))

d = np.cross(n1, n2)                                # direction of the line of intersection
p0 = LA.lstsq(np.vstack((n1, n2)), -np.array([e1, e2]), rcond=None)[0]
print("line direction:", d, " point:", p0)
for n, e in planes:
    print("contains the line:", np.isclose(n @ p0 + e, 0), np.isclose(n @ d, 0))

X, Y = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
for (n, e), col in zip(planes, ("C0", "C1")):
    ax.plot_surface(X, Y, (-e - n[0] * X - n[1] * Y) / n[2], alpha=0.4, color=col)
s = np.linspace(-0.25, 0.25, 20)
L = p0.reshape(-1, 1) + d.reshape(-1, 1) * s
ax.plot(L[0], L[1], L[2], "k", lw=3)
ax.set_zlim(-6, 6)
ax.scatter([0], [0], [0], color="red")
ax.text(0, 0, 0, "$O$")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
plt.savefig(os.path.join(FIG, "cbXIIq30b.pdf"), bbox_inches="tight")
