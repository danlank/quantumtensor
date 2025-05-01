import numpy as np
import By_part_entanglement as bpe
from state_visualization import visualize_state 
import matplotlib.pyplot as plt
import single_qubit_gates as sqg
import two_qubit_gates as tqg
import Single_qubit_operation as sqo
import two_qubit_operation as tqo


def plot_entropy(state,N):
    H=sqg.Hadamard()
    X=sqg.X_gate()
    T = np.array([[1, 0], [0, np.exp(-1j * np.pi / 4)]])
    CX=tqg.CX
    gates = [H, X, T]
    m=20
    for i in range(m):
        for j in range(1,N+1):
            random_index = np.random.choice(len(gates))  
            selected_gate = gates[random_index]
            state= sqo.Single_qubit_operation(state, N,j,selected_gate)
            
        for k in range(1,N):
            state = tqo.two_qubit_operation(state,N,k,k+1, CX)
            
    state = state / np.linalg.norm(state)  
    x_values = []
    s_values = []
    for x in range(1,N) : 
         s=bpe.By_part_entanglement(state, N, x)
         x_values.append(x)
         s_values.append(s)
            
    plt.plot(x_values, s_values, marker='o', linestyle='-', color='b', label="s vs x")
    plt.xlabel("x")
    plt.ylabel("s")
    plt.title("Plot of x vs. s")
    plt.legend()
    plt.show()
    
    return()

N=5
#state = np.zeros(2**N, dtype=complex)
#state[1] = 1
a = np.random.normal(0, 0.5, 2**N)  # Real part
b = np.random.normal(0, 0.5, 2**N)  # Imaginary part
state = a + 1j * b  
state = state / np.linalg.norm(state)
plot_entropy(state, N)
