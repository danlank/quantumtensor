import numpy as np

def By_part_entanglement(psi, N, s):
    if not np.isclose(np.linalg.norm(psi), 1):
        raise ValueError("Input state psi must be normalized.")
    
    a = np.reshape(psi, (2**s, 2**(N-s)))
    v = np.linalg.svd(a, compute_uv=False)  # Singular values
    S = -np.sum(v**2 * np.log(v**2 + 1e-20))  # Von Neumann entropy
    print("Singular values (v):", v)
    return S

N = 4
s = 2

# Define a normalized random quantum state
psi = np.random.rand(2**N) + 1j * np.random.rand(2**N)
psi /= np.linalg.norm(psi)  # Normalize the state

S = By_part_entanglement(psi, N, s)
print("Entanglement entropy:", S)
