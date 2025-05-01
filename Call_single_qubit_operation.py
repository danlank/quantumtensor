import numpy as np
from Single_qubit_operation import Single_qubit_operation  
import single_qubit_gates as sqg 
def Call_SQO():
    N = 4
    C = 0
    site = 2
    State = np.zeros(2**N, dtype=np.complex128) 
    State[0] = 1 
    State[2]=1
    #B = sqg.Hadamard() 
    B = np.array([[1, 0], [0, 0]])
    state = Single_qubit_operation(State, N, site, B)  
    print("Final state after operation:")
    print(state)
    
    return state

Call_SQO()

