import numpy as np
from table import  Table
import heapq
from note import Note

"""
Name: David Graber
Email: D3217453@gmail.com
Date: 18/11/2025
"""

# Breadth-First Search implementation
# Creates initial Note, checks goal, expands nodes level by level
def BFS(array):
    stok = []
    note = Note(np.array([array[0:3], array[3:6], array[6:9]], dtype='uint8'), None, -1, 0)
    expanded = 0
    table = Table() # visited states

    table.insert(note) # Check if already solved
    stok.append(note)

    if note.targetstate():
        return topath(note), expanded, note.cost

    while len(stok) != 0:
        note = stok.pop(0)


        expanded += 1
        notes = note.expand()

        for note in notes:
            if note.targetstate():
                return topath(note), expanded, note.cost

            if table.insert(note):
                stok.append(note)

    return None

# A* Search implementation
# Uses priority queue based on cost + heuristics
def Astar(array):
    note = Note(np.array([array[0:3], array[3:6], array[6:9]], dtype='uint8'), None, -1, 0)
    expanded = 0
    table = Table() # visited states
    heap = [] # priority queue

    table.insert(note)
    heapq.heappush(heap, note)

    while len(heap) != 0:
        note = heapq.heappop(heap)

        if note.targetstate():
            return topath(note), expanded, note.cost

        expanded += 1
        notes = note.expand()

        for note in notes:
            if table.insert(note):
                heapq.heappush(heap, note)

    return None


# Builds the solution path by traversing backward from the goal Notepy .\Tiles.py 1 4 0 5 8 2 3 6 7
def topath(note):

    path = ""

    while note.father is not None:
        path += str(note.action)
        note = note.father

    return path[::-1]




