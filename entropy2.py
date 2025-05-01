
import numpy as np
import By_part_entanglement as bpe
from state_visualization import visualize_state 
import matplotlib.pyplot as plt
import single_qubit_gates as sqg
import two_qubit_gates as tqg
import Single_qubit_operation as sqo
import two_qubit_operation as tqo

def plot_entropy(state, N):
 
    H = sqg.Hadamard()
    X = sqg.X_gate()
    T = np.array([[1, 0], [0, np.exp(-1j * np.pi / 4)]])
    CX = tqg.CX
    gates = [H, X, T]  # Single-qubit gates only

    # Apply random quantum gates
    m = 20 # Number of random operations
    for _ in range(m):
        for j in range(1, N+1):  # Avoid out-of-bounds indexing
            random_index = np.random.choice(len(gates))  
            selected_gate = gates[random_index]
            state = sqo.Single_qubit_operation(state, N, j, selected_gate)

        # Apply CX (two-qubit) gates randomly
        for j in range(1, N):  # Ensure (j+1) does not exceed N
            state = tqo.two_qubit_operation(state, N, j, j+1, CX)

    # Normalize final state
    state = state / np.linalg.norm(state)  

    # Compute entanglement entropy for different bipartitions
    x_values = []
    s_values = []
    for x in range(1, N):  # x must be in [1, N-1]
        s = bpe.By_part_entanglement(state, N, x)
        x_values.append(x)
        s_values.append(s)
    
    # Plot entropy
    plt.plot(x_values, s_values, marker='o', linestyle='-', color='b', label="s vs x")
    plt.xlabel("Bipartition x")
    plt.ylabel("Von Neumann Entropy (S)")
    plt.title("Bipartite Entanglement Entropy")
    plt.legend()
    plt.show()
    
    return

# Define a 5-qubit initial state
N = 5
state = np.zeros(2**N, dtype=complex)
state[1] = 1  # Initialize in computational basis |00001⟩

plot_entropy(state, N)
