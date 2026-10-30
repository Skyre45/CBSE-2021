# Cards numbered 1..20: events as subsets of a uniform sample space
# Adapted from {https://github.com/gadepall/probability}
import os
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
n = np.arange(1, 21)
pmf = np.full(n.size, 1 / 20)                    # p(n) = 1/20

# sieve of Eratosthenes
is_prime = np.ones(21, dtype=bool); is_prime[:2] = False
for p in range(2, 5):
    is_prime[p * p::p] = False
prime = is_prime[1:]
odd = n % 2 == 1
composite = (n > 1) & ~prime

P = lambda E: Fraction(int(E.sum()), 20)
print("(i)   P(odd prime)  =", P(prime & odd))
print("(ii)  P(composite)  =", P(composite))
L = int(np.lcm.reduce([3, 6, 9]))
print("(iii) lcm(3,6,9) =", L, " P =", P(n % L == 0))
L2 = int(np.lcm(3, 7))
print("(iv)  lcm(3,7) =", L2, " P =", P(n % L2 == 0))
even = ~odd
print("(v)   P(prime | even) =", P(prime & even) / P(even))

# plotting
plt.figure(figsize=(8, 3.8))
plt.stem(n[prime], pmf[prime], linefmt="C0-", markerfmt="C0o", basefmt=" ", label="prime")
plt.stem(n[composite], pmf[composite], linefmt="C1-", markerfmt="C1s", basefmt=" ", label="composite")
plt.stem(n[n == 1], pmf[n == 1], linefmt="C2-", markerfmt="C2^", basefmt=" ", label="neither")
plt.xticks(n)
plt.ylim(0, 0.07)
plt.xlabel("$n$"); plt.ylabel("$p_X(n)$")
plt.legend(ncol=3, loc="upper center"); plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig(os.path.join(FIG, "cbXq20.pdf"), bbox_inches="tight")
