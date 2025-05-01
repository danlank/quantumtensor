import numpy as np
from state_visualization import visualize_state  

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

def Call_SQO():
    N = 3
    C = 0
    site = 1
    State = np.zeros(2**N, dtype=np.complex128) 
    State[C] = 1  
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
    state = Single_qubit_operation(State, N, site, H)  
    print("state after operation H:")
    print(state)
    visualize_state(state, 3)
    return state



def two_qubit_operation(state, N, p,q, B):
    final_state = np.zeros_like(state, dtype=np.complex128)
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
         
         
         b0 = B[u, 0] * state[v0]
         b1 = B[u, 1] * state[v1]
         b2 = B[u, 2] * state[v2]  
         b3 = B[u, 3] * state[v3]
         final_state[v] = b0+b1+b2+b3
     
    return final_state

def Call_tqo():
   
    p = 1
    q = 2
    state=Call_SQO()
    B = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]) 

    state_f = two_qubit_operation(state, 3, p,q, B)
   
    print("Final state after operation cx gate:")
    print(state_f)
    visualize_state(state_f, 3)
    return state_f

def By_part_entanglement(state_f, N, s):
    #if not np.isclose(np.linalg.norm(state_f), 1):
        #raise ValueError("Input state psi must be normalized.")
    
    a = np.reshape(state_f, (2**s, 2**(N-s)))
    v = np.linalg.svd(a, compute_uv=False)  # Singular values
    S = -np.sum(v**2 * np.log(v**2 + 1e-20))  # Von Neumann entropy
    print("Singular values (v):", v)
    return S


s = 2
state_f = Call_tqo()
S = By_part_entanglement(state_f, 3, s)
print("Entanglement entropy:", S)


  