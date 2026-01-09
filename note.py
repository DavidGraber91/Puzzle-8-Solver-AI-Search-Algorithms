
"""
Name: David Graber
Email: D3217453@gmail.com
Date: 18/11/2025

Represents a node/state in the puzzle search tree.
Each node stores its puzzle state, parent node, action taken, and cost.
"""
import numpy as np

# Board size for the puzzle (3x3)
SIZE = 3

# Constants for indexing
ROW = 0
COL = 1

# Representation of empty space in the puzzleSPASE = 0
SPASE = 0

# Actions
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

# Default movement cost
DEF_COST = 1


class Note:

    def __init__(self, state, father, action, cost):
        self.state = state
        self.father = father
        self.action = action
        self.cost = cost

    # Comparison operator for priority queues using f(n) = g(n) + h(n)
    def __lt__(self, other):
        return self.cost + self.heuristics() < other.cost + other.heuristics()

    # Move the empty space left, if possible
    def left(self):
        index = self.getspase()

        # check if possible
        if index[COL] == 0:
            return None

        newstate = self.state.copy()

        # Swap with left neighbor to the new state
        newstate[index[ROW], index[COL]] = newstate[index[ROW], index[COL] - 1]
        newstate[index[ROW] , index[COL] - 1] = SPASE

        # Create new node with updated state
        newnote = Note(newstate, self, newstate[index[ROW], index[COL]], self.cost + DEF_COST)
        return newnote

    # Move the empty space right, if possible
    def right(self):
        index = self.getspase()
        if index[COL] == SIZE - 1:
            return None
        newstate = self.state.copy()
        newstate[index[ROW], index[COL]] = newstate[index[ROW], index[COL] + 1]
        newstate[index[ROW] , index[COL] + 1] = SPASE

        newnote = Note(newstate, self, newstate[index[ROW], index[COL]], self.cost + DEF_COST)
        return newnote

    # Move the empty space upward, if possible
    def up(self):
        index = self.getspase()
        if index[ROW] == 0:
            return None
        newstate = self.state.copy()
        newstate[index[ROW], index[COL]] = newstate[index[ROW] - 1, index[COL]]
        newstate[index[ROW] - 1 , index[COL]] = SPASE

        newnote = Note(newstate, self, newstate[index[ROW], index[COL]], self.cost + DEF_COST)
        return newnote

    # Move the empty space downward, if possible
    def down(self):
        index = self.getspase()
        if index[ROW] == SIZE - 1:
            return None
        newstate = self.state.copy()
        newstate[index[ROW], index[COL]] = newstate[index[ROW] + 1, index[COL]]
        newstate[index[ROW] + 1 , index[COL]] = SPASE

        newnote = Note(newstate, self, newstate[index[ROW], index[COL]], self.cost + DEF_COST)
        return newnote

    """
    Generate all valid successor states (children) from current state
    by applying each possible movement.
    """
    def expand(self):

        temp = self.left()
        arr = []

        if temp is not None:
            arr.append(temp)

        temp = self.right()
        if temp is not None:
            arr.append(temp)

        temp = self.up()
        if temp is not None:
            arr.append(temp)

        temp = self.down()
        if temp is not None:
            arr.append(temp)

        return arr

    """
    Heuristic evaluation function (Manhattan distance + penalty).
    Returns 0 if goal state.
    """
    def heuristics(self):

        #if goal state
        if self.targetstate():
            return 0

        g = 0

        # Manhattan distance for each tile
        for i in range(SIZE):
            for j in range(SIZE):
                if self.state[i][j] != SPASE:
                    g += abs((self.state[i][j] % SIZE) - j)
                    g += abs(int(self.state[i][j] / SIZE) - i)

        # Add 2 if movement seems unhelpful
        if self.backstep():
            g += 2

        return g

    """
    Detects whether the previous move likely reversed progress,
    adding a penalty to discourage backtracking.
    """
    def backstep(self):

        index = self.getspase()

        if index[ROW] != 0 and int(self.state[index[ROW] - 1, index[COL]] / SIZE) >= index[ROW]:
            return False
        if index[ROW] != SIZE - 1 and int(self.state[index[ROW] + 1, index[COL]] / SIZE) <= index[ROW]:
            return False
        if index[COL] != 0 and self.state[index[ROW], index[COL] - 1] % SIZE >= index[COL]:
            return False
        if index[COL] != SIZE - 1 and self.state[index[ROW], index[COL] + 1] % SIZE <= index[COL]:
            return False

        return True

    # Locate the empty tile (0) in the puzzle state
    def getspase(self):
        return np.argwhere(self.state == SPASE)[0]

    # Check whether current state matches the goal state (0..8 in order)
    def targetstate(self):
        for i in range(SIZE):
            for j in range(SIZE):
                if self.state[i][j] != i * SIZE + j:
                    return False
        return True





