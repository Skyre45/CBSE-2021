# Relation 'x and y have a letter in common' as a boolean matrix
import os
import numpy as np
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
words = ["at", "tip", "pin", "dog", "god", "nod", "sky"]
letters = "abcdefghijklmnopqrstuvwxyz"
L = np.array([[ch in w for ch in letters] for w in words], dtype=int)   # word-letter incidence
M = (L @ L.T) > 0                                                        # M[i,j] = x_i R x_j
print("reflexive :", bool(np.all(np.diag(M))))
print("symmetric :", bool(np.array_equal(M, M.T)))
T = (M.astype(int) @ M.astype(int)) > 0                                  # x_i R x_j R x_k
bad = np.argwhere(T & ~M)
print("transitive:", not len(bad))
for i, k in bad:
    j = [j for j in range(len(words)) if M[i, j] and M[j, k]][0]
    print("  %s R %s, %s R %s but %s not R %s" % (words[i], words[j], words[j], words[k], words[i], words[k]))

fig, ax = plt.subplots(1, 2, figsize=(10, 4.5))
for a, mat, t in zip(ax, (M, T), ("$M$ (relation $R$)", "$M^2>0$ (two-step)")):
    a.imshow(mat, cmap="Blues", vmin=0, vmax=1.6)
    a.set_xticks(range(len(words))); a.set_xticklabels(words, rotation=45)
    a.set_yticks(range(len(words))); a.set_yticklabels(words); a.set_title(t)
for i, k in bad:
    ax[1].plot(k, i, "rx", ms=10)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "cbXIIq21a.pdf"), bbox_inches="tight")
