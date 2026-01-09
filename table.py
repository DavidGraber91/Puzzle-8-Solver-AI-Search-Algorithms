import numpy as np

"""
Name: David Graber
Email: D3217453@gmail.com
Date: 18/11/2025


Hash table-like structure used to store explored puzzle states.
Each index holds a list of Note objects with the same computed hash.
Used mainly to detect repeated states and avoid re-exploration.
"""

class Table:

    # Initialize array with fixed size (100000 slots), each starting as None
    def __init__(self):
        self.arr = np.full(100000, None)

    """
    Inserts a Note into the table.
    If a state with the same board configuration already exists, keeps only the lower-cost version.
    Returns True if inserted or replaced, False if ignored.
    """
    def insert(self, note):
        index = Table.fun(note)

        # If slot empty, create new list and insert
        if self.arr[index] is None:
            self.arr[index] = [note]
            return True

        # If slot is not empty, check for identical states
        for _note in self.arr[index]:
            if np.array_equal(note.state, _note.state): # Compare board configurations
                if note.cost < _note.cost: # If new Note has lower cost, replace old one
                    self.arr[index].remove(_note)
                    self.arr[index].append(note)
                    return True
                else: # Same state but higher cost, ignore
                    return False

        # No identical state found, append to list
        self.arr[index].append(note)
        return True

    """
    Custom hash function for Note states.
    Builds a 5-digit number based on specific tile positions:
    - (0,0)
    - (0,2)
    - (1,1)
    - (2,0)
    - (2,2)
    Used to distribute states into hash table.
    """
    @staticmethod
    def fun(note):
        index = 0
        index += note.state[0][0]
        index *= 10

        index += note.state[0][2]
        index *= 10

        index += note.state[1][1]
        index *= 10

        index += note.state[2][0]
        index *= 10

        index += note.state[2][2]

        return index