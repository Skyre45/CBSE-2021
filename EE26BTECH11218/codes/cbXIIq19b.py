# A^2 = A  =>  (2I + A)^3 - 19A = 8I : Eigenvalues and eigenvectors
import os
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")

# Define an idempotent matrix A where A^2 = A
A = np.array([[2, -2], [1, -1]]) 

# Verify A^2 = A
assert np.allclose(np.linalg.matrix_power(A, 2), A)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", np.round(eigenvalues, 4))

# Evaluate matrix polynomial (2I + A)^3 - 19A
I = np.eye(2)
result_matrix = np.linalg.matrix_power(2*I + A, 3) - 19*A
print("Result of (2I + A)^3 - 19A:\n", result_matrix)
print("Expected: 8I\n", 8*I)

# Plot the scalar polynomial mapping for the eigenvalues
lambda_vals = np.linspace(-1, 2, 100)
p_lambda = (2 + lambda_vals)**3 - 19 * lambda_vals

plt.plot(lambda_vals, p_lambda, 'b-', label=r'$p(\lambda) = (2+\lambda)^3 - 19\lambda$')
plt.plot([0, 1], [8, 8], 'ro') # The eigenvalues mapped
plt.annotate('(0, 8)', xy=(0, 8), xytext=(-0.3, 8.5))
plt.annotate('(1, 8)', xy=(1, 8), xytext=(1.1, 7))

plt.xlabel(r'$\lambda$')
plt.ylabel(r'$p(\lambda)$')
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.savefig(os.path.join(FIG, "cbXIIq19b.pdf"), bbox_inches="tight")
