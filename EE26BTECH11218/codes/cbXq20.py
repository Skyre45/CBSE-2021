# Cards numbered 1..20: exact probabilities from the PMF p_X(n) = 1/20 against the C simulation
import os
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(DIR, "..", "figs")
n = np.arange(1, 21)
pmf = np.full(n.size, 1 / 20)                           # p_X(n) = 1/20

is_prime = np.ones(21, dtype=bool); is_prime[:2] = False
for p in range(2, 5):
    is_prime[p * p::p] = False
prime = is_prime[1:]
even = n % 2 == 0
composite = (n > 1) & ~prime

# P(E) = P(Y_E = 1) = sum of p_X(n) over the n in E
exact = np.array([pmf[prime & ~even].sum(),               # (i)   odd prime
                  pmf[composite].sum(),                   # (ii)  composite
                  pmf[n % 18 == 0].sum(),                 # (iii) multiple of 3, 6 and 9
                  pmf[n % 21 == 0].sum(),                 # (iv)  multiple of 3 and 7
                  pmf[prime & even].sum() / pmf[even].sum()])   # (v) P(prime | X even), from p_{X|E}
for k, e in enumerate(exact):
    print("(%s) exact = %s = %.4f" % ("i ii iii iv v".split()[k], Fraction(e).limit_denominator(100), e))

sim = np.loadtxt(os.path.join(DIR, "cbXq20.dat"))       # columns: part, estimate from the C program
x = sim[:, 0].astype(int)
plt.figure(figsize=(7, 4))
plt.stem(x, sim[:, 1], markerfmt="o", linefmt="C0-", label="Simulation (C)")
plt.stem(x, exact, markerfmt="x", linefmt="C3--", label="Analysis")
plt.xticks(x, ["(i)", "(ii)", "(iii)", "(iv)", "(v)"])
plt.xlabel("Part"); plt.ylabel("Probability")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXq20.pdf"), bbox_inches="tight")
