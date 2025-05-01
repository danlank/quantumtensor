import numpy as np

def Single_qubit_operation(State, N, site, B):
    final_state = np.zeros_like(State, dtype=np.complex128)
    a = 2**(N - site)
    
    for r in range(2**N):
        q=int((a & r)/a)
        q1=1^q
        r1 = r ^ a
        
        a1 = B[q, q] * State[r]
        a2 = B[q, q1] * State[r1]
        
        final_state[r] = a1 + a2 
    
    return final_state



