import numpy as np
import single_qubit_gates as sqg

def measure_first_qubit_z_basis(psi):
    
    #Perform a Z-basis measurement on the first qubit of a two-qubit state.
    # def a function with parameter psi--> 4-element complex array representing the two-qubit state vector.
     #The measurement outcome, either +1 or -1.
   
    z = sqg.Z_gate()  # calling Z-gate 
    projector_0 = (np.eye(2) + z) / 2  # Projector for outcome +1 (state |0⟩).
    projector_1 = (np.eye(2) - z) / 2  # Projector for outcome -1 (state |1⟩).
    
    # Apply the projectors to the first qubit.
    projector_0_first_qubit = np.kron(projector_0, np.eye(2))
    projector_1_first_qubit = np.kron(projector_1, np.eye(2))
    
    # Calculate probabilities for each outcome.
    prob_0 = np.vdot(psi, projector_0_first_qubit @ psi)  # Probability of outcome +1.
    prob_1 = np.vdot(psi, projector_1_first_qubit @ psi) # Probability of outcome -1.
    
    # generating a random value and compairing it with probability of outcome +1.
    #depending upon that define post measurement state.
    random_value = np.random.random()
    
    if random_value < prob_0:
        outcome = 1
        psi_post_measurement = (projector_0_first_qubit @ psi) / np.sqrt(prob_0) # Normalize the post-measurement state
    else:
        outcome = -1
        psi_post_measurement = (projector_1_first_qubit @ psi) / np.sqrt(prob_1)
    
    return outcome, psi_post_measurement

def measure_second_qubit_z_basis(psi):
    """
    Perform a Z-basis measurement on the second qubit of a two-qubit state.
    """
    z = sqg.Z_gate()  # Z-gate (Pauli-Z)
    projector_0 = (np.eye(2) + z) / 2  # Projector for outcome +1 (state |0⟩)
    projector_1 = (np.eye(2) - z) / 2  # Projector for outcome -1 (state |1⟩)
    
    # Apply the projectors to the second qubit
    projector_0_second_qubit = np.kron(np.eye(2), projector_0)
    projector_1_second_qubit = np.kron(np.eye(2), projector_1)
    
    # Calculate probabilities for each outcome
    prob_0 = np.vdot(psi, projector_0_second_qubit @ psi)
    prob_1 = np.vdot(psi, projector_1_second_qubit @ psi)
    
    # Randomly determine the measurement outcome
    random_value = np.random.random()
    
    if random_value < prob_0:
        outcome = 1
        psi_post_measurement = (projector_0_second_qubit @ psi) / np.sqrt(prob_0)
    else:
        outcome = -1
        psi_post_measurement = (projector_1_second_qubit @ psi) / np.sqrt(prob_1)
    
    return outcome, psi_post_measurement

def demonstrate_measurement():
    """
    Demonstrate the effect of Z-basis measurements on a two-qubit state.
    """
    # Define and normalize the initial two-qubit state
    psi = np.array([3/5, 4/5, 1/5, 2/5]) + 0j
    psi = psi / np.linalg.norm(psi)
    
    # Perform Z-basis measurement on the first and second qubits
    outcome_first, psi_after_first = measure_first_qubit_z_basis(psi)
    outcome_second, psi_after_second = measure_second_qubit_z_basis(psi)
    
    # Print the measurement outcomes and post-measurement states
    print(f"Measurement outcome for the first qubit: {outcome_first}")
    print(f"Post-measurement state after first qubit measurement: {psi_after_first}")
    print(f"Measurement outcome for the second qubit: {outcome_second}")
    print(f"Post-measurement state after second qubit measurement: {psi_after_second}")

# Run the demonstration function
demonstrate_measurement()

# Define the controlled-X (CNOT) gate for two qubits
cx = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 1, 0]])

# Define the initial state |00⟩
psi0 = np.array([1, 0, 0, 0]) + 0j

# Apply Hadamard gate on the first qubit
H = sqg.Hadamard()
psi1 = np.kron(H, np.eye(2)) @ psi0

# Apply the CNOT gate
psi2 = cx @ psi1

# Perform measurements on the resulting states
result_1st_qubit_psi1, state_after_1st_measurement = measure_first_qubit_z_basis(psi1)
result_2nd_qubit_psi1, state_after_2nd_measurement = measure_second_qubit_z_basis(state_after_1st_measurement)

result_1st_qubit_psi2, state_after_3rd_measurement = measure_first_qubit_z_basis(psi2)
result_2nd_qubit_psi2, state_after_4th_measurement = measure_second_qubit_z_basis(state_after_3rd_measurement)

# Print the measurement outcomes for the sequences of operations
print(f"Measurement outcomes for psi1: first qubit = {result_1st_qubit_psi1}, second qubit = {result_2nd_qubit_psi1}")
print(f"Measurement outcomes for psi2: first qubit = {result_1st_qubit_psi2}, second qubit = {result_2nd_qubit_psi2}")