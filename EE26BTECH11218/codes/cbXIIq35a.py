# Area between x = y^2 and x = 4 split equally by x = a
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
from scipy.integrate import quad
from scipy.optimize import brentq

A = lambda a: quad(lambda x: 2 * np.sqrt(x), 0, a)[0]      # area of the part with x <= a
total = A(4)
a = brentq(lambda t: A(t) - total / 2, 0.1, 4)
print("total area =", total, " 32/3 =", 32 / 3)
print("a =", a, " 4^(2/3) =", 4 ** (2 / 3), " check:", A(a), total - A(a))

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
