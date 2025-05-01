import numpy as np


def two_qubit_operation(State, N, p,q, B):
    final_state = np.zeros_like(State, dtype=np.complex128)
    a1 = 2**(N - p)
    a2 = 2**(N - q)
    for v in range(2**N):
         r=int((a1 & v)/a1)
         s=int((a2 & v)/a2)
         u=2*r+s
         w=a1+a2
         v3=v | w
         v0=w^ v3
         v1=a1^ v3
         v2=a2^ v3
         
         
         b0 = B[u, 0] * State[v0]
         b1 = B[u, 1] * State[v1]
         b2 = B[u, 2] * State[v2]  
         b3 = B[u, 3] * State[v3]
         final_state[v] = b0+b1+b2+b3
     
    return final_state

