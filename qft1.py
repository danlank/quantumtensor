import numpy as np
import single_qubit_gates as sqg
import two_qubit_gates as tqg
import Single_qubit_operation as sqo
import two_qubit_operation as tqo
import state_visualization as sv

def qft(state, N):

   
    psi = state

    for i in range(4):

        psi = sqo.Single_qubit_operation(psi, N,1,sqg.Hadamard())

        for j in range(4-i-1):
            psi = tqo.two_qubit_operation(psi,N,j+1,j+2, tqg.Swap @ tqg.CRk(j+1))
    
    return psi

state = np.zeros(2**4, dtype=complex)
state[1] = 1

ff = np.fft.fft(state, norm='ortho')
print(np.fft.fft(state, norm='ortho'))

print()

psi = qft(state, 4)
print(psi)

print()
sv.visualize_state(ff, 4)
print()
sv.visualize_state(psi, 4)

print(np.allclose(ff, psi))

