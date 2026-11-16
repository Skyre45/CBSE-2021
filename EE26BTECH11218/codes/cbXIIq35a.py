# Area between x = y^2 and x = 4 split equally by x = a (a computed by the C program)
import os
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")
a = float(np.loadtxt(os.path.join(DIR, "cbXIIq35a.dat")))
print("a =", a, " 4^(2/3) =", 4 ** (2 / 3))

y = np.linspace(-2, 2, 400)
plt.figure(figsize=(6, 5))
plt.plot(y ** 2, y, "b", label="$x=y^2$")
plt.plot([4, 4], [-2, 2], "k", label="$x=4$")
plt.plot([a, a], [-np.sqrt(a), np.sqrt(a)], "r", label="$x=a$")
plt.fill_betweenx(y, y ** 2, a, where=y ** 2 <= a, alpha=0.3, color="C0")
plt.fill_betweenx(y, np.maximum(y ** 2, a), 4, alpha=0.3, color="C1")
plt.xlabel("$x$"); plt.ylabel("$y$"); plt.title("$a=%.4f$" % a)
plt.legend(loc="upper left"); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXIIq35a.pdf"), bbox_inches="tight")
