# Car approaching a tower: angle of depression 30 deg -> 60 deg in 18 min
# Helper functions adapted from {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from cbfuncs import line_gen, ang_vec
from cbfuncs import label_pts

s3 = np.sqrt(3.0)
for h in [10.0, 50.0, 120.0]:                  # the height drops out
    # x(0) = x0 = h/tan30,  x(18) = x0 - 18 v = h/tan60   ->  unknowns (x0, v)
    M = np.array([[1.0, 0.0], [1.0, -18.0]])
    d = np.array([h * s3, h / s3])
    x0, v = LA.solve(M, d)
    t_star = (h / s3) / v                      # x(18 + t) = 0
    print(f"h = {h:5.0f}: x0 = {x0:8.3f}, v = {v:7.4f}, time to reach tower = {t_star:.4f} min")

h = 50.0
x0, v = LA.solve(M, np.array([h * s3, h / s3]))
T_top = np.array([[0.0], [h]])
X = lambda t: np.array([[x0 - v * t], [0.0]])
C1, C2, C3 = X(0), X(18), X(27)
for C in (C1, C2):
    ang = np.degrees(ang_vec(np.array([[-1.0], [0.0]]), T_top - C))
    print("angle of depression =", ang)

# plotting
plt.figure(figsize=(8, 4.5))
for Cx, col in ((C1, "r"), (C2, "g")):
    xl = line_gen(T_top, Cx)
    plt.plot(xl[0, :], xl[1, :], col)
xg = line_gen(C1, np.array([[0.0], [0.0]]))
plt.plot(xg[0, :], xg[1, :], "k")
xt = line_gen(np.array([[0.0], [0.0]]), T_top)
plt.plot(xt[0, :], xt[1, :], "k", lw=3)
pts = np.block([[T_top, C1, C2, C3]])
plt.scatter(pts[0, :], pts[1, :], color="blue", zorder=5)
label_pts(pts, ["$T$", r"$C_1$ ($30^\circ$)", r"$C_2$ ($60^\circ$)", r"$B$ ($t=27$ min)"])
plt.xlabel("$x$ (m)"); plt.ylabel("$y$ (m)")
plt.axis("equal"); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXq35.pdf"), bbox_inches="tight")
