import numpy as np
from Single_qubit_operation import Single_qubit_operation  
import single_qubit_gates as sqg 
import diracnotation as dn
import Call_single_qubit_operation as csqo


def z_measurement(state, site, N, State):
   
   
    P_0 = np.array([[1, 0], [0, 0]], dtype=np.complex128)

    
    phi =Single_qubit_operation(psi, N, site, P_0)
   
    print("Projected state phi:",dn.array_to_dirac(phi) )

    pro_0 = np.real(np.vdot(psi, phi))  # Probability must be real-valued
    print("Probability of measuring |0>: ", pro_0)

    # Generate a random number to simulate measurement outcome
    r = np.random.random()
    #print("Random number for measurement:", r)

    if r < pro_0:
        final_state = phi / np.sqrt(pro_0) if pro_0 > 1e-10 else phi  # Normalize safely
        outcome = 1
    else:
        outcome = -1
        pro_1 = 1 - pro_0
        eps = 1e-10  # To avoid division by zero
        final_state = (state - phi) / np.sqrt(max(pro_1, eps))  

    

    return outcome, final_state

# Example Usage
N = 2  # Number of qubits
site = 1  # Measure qubit at index 1
State = np.zeros(2**N, dtype=np.complex128) 
State[0]=1
State[1]=1
State[2]=1
State[3]=1
psi=State/np.sqrt(np.dot(State,State))
print(dn.array_to_dirac(psi)) 
trial=3
for i in range(trial):
    outcome, final_state = z_measurement(State, site, N, State) #calling the measurement function
    print("s",dn.array_to_dirac(final_state))
    print("outcome",outcome)
    print ("state",final_state)



