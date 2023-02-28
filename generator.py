import pennylane as qml

dev = qml.device("default.qubit", wires=1)

def random_circuit (num_qubits:int, depth:int, basis_gates:list):

    """
        Design a function that generates a random quantum circuit by 
        considering as parameters the number of qubits, the number of depths,
        and the base of gates to be used. You could only use the quantum 
        gates of 1 and 2 qubits.
    """
    
    """
        the general idea is: 

            1.  check for depth, create a list of qubits open for insert
            2.  selete a gate at random
            3.  based on the gate property (single/multiple qubits) select
                random qubit(s)
            4.  add the gate and update depth
    """

    return 0

class RandomCircuitGenerator:
    def __init__(self, num_qubits:int, depth:int, basis_gates:list) -> None:
        self.num_qubits = num_qubits
        self.depth = depth
        self.basis_gates = basis_gates
        self.circuit = Circuit()
    
class Circuit:
    def __init__(self) -> None:
        self.depth=0
        self.basis_gates = []
        self.num_qubits=0
        self.circuit=None


    def __init__(self, num_qubits:int, depth:int, basis_gates:list) -> None:
        self.num_qubits = num_qubits
        self.depth = depth
        self.basis_gates = basis_gates
        self.circuit = qml.device('default.qubit', wires=num_qubits)
    
    def getdepth(self):
        return self.depth

    def getbasis(self):
        return self.basis_gates

    def getnumqubits(self):
        return self.num_qubits
    
    def getcircuit(self):
        return self.circuit

    def addgate(self, qubit, gate):
        return 0
    

    

