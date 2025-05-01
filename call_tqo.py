import numpy as np
from two_qubit_operation import two_qubit_operation 
from state_visualization import visualize_state  
def Call_tqo():
    N = 4
    p = 1
    q = 2
    C=4
    State = np.zeros(2**N, dtype=np.complex128) 
    State[C] = 1  
    B = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]) 

    state = two_qubit_operation(State, N, p,q, B)  
    print("Final state after operation:")
    print(state)
    
    return state

state = Call_tqo()
visualize_state(state, 4)

