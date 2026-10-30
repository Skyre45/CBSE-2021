# Collinearity: b x c + c x a + a x b = (b-a) x (c-a) = 0 iff A, B, C are collinear
# Adapted from {https://github.com/gadepall/matgeo/tree/main/codes/book/cross.py}
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy.linalg as LA

S = lambda a, b, c: np.cross(b, c) + np.cross(c, a) + np.cross(a, b)
a = np.array([1.0, 0.0, 2.0])
b = np.array([3.0, 1.0, 1.0])
c_col = a + 2.5 * (b - a)                          # on the line AB
c_non = np.array([2.0, 3.0, 4.0])                  # not on the line AB

for name, c in (("collinear", c_col), ("not collinear", c_non)):
    s = S(a, b, c)
    sa, sb, sc = LA.norm(b - c), LA.norm(c - a), LA.norm(a - b)
    p = (sa + sb + sc) / 2
    heron = np.sqrt(max(p * (p - sa) * (p - sb) * (p - sc), 0))
    print(name, ": S =", s, " (b-a)x(c-a) =", np.cross(b - a, c - a), " |S|/2 =", LA.norm(s) / 2, " Heron area =", heron)

fig = plt.figure(figsize=(10, 4.5))
for i, (c, t) in enumerate(((c_col, "collinear: $S=\\mathbf{0}$"), (c_non, "not collinear: $S\\perp$ plane"))):
    ax = fig.add_subplot(1, 2, i + 1, projection="3d")
    P = np.vstack((a, b, c, a))
    ax.plot(P[:, 0], P[:, 1], P[:, 2], "b-o")
    for pt, nm in zip((a, b, c), "ABC"):
        ax.text(pt[0], pt[1], pt[2], nm)
    s = S(a, b, c)
    if LA.norm(s) > 1e-9:
        g = (a + b + c) / 3
        ax.quiver(g[0], g[1], g[2], s[0], s[1], s[2], color="r", length=0.4)
    ax.set_title(t)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
plt.tight_layout()
plt.savefig(os.path.join(FIG, "cbXIIq29.pdf"), bbox_inches="tight")
