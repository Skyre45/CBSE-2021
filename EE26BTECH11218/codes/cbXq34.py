# Volume of water pumped through a circular pipe: flux integral and time integral
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad, cumulative_trapezoid

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
R, v, T = 4.0, 80.0, 3600.0                  # cm, cm/s, s

# flux Q = integral of v over the cross-section, in polar coordinates (cm^3/s)
Q, err = dblquad(lambda rho, th: v * rho, 0, 2 * np.pi, 0, R)
print("Q numeric =", Q, " pi R^2 v =", np.pi * R ** 2 * v)

# V(t) = integral of Q dt  (cm^3 -> litres)
t = np.linspace(0, T, 721)
Vt = cumulative_trapezoid(Q * np.ones_like(t), t, initial=0) / 1000.0
print("V(1 h) =", Vt[-1], "litres;  exact 4608*pi =", 4608 * np.pi)
print("with pi = 22/7:", 4608 * 22 / 7)

# plotting
plt.plot(t / 60.0, Vt, "b", lw=2)
P = np.array([[60.0], [Vt[-1]]])
plt.scatter(P[0], P[1], color="red", zorder=5)
plt.annotate(f"({P[0,0]:.0f} min, {P[1,0]:.1f} L)", (P[0, 0], P[1, 0]), textcoords="offset points", xytext=(-80, -15))
plt.xlabel("$t$ (min)"); plt.ylabel("$V(t)$ (litres)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXq34.pdf"), bbox_inches="tight")
