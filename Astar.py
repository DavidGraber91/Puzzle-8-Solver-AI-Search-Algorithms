import numpy as np
from table import  Table
from note import Note
import heapq

def Astar(array):
    note = Note(np.array([array[0:3], array[3:6], array[6:9]], dtype='uint8'), None, -1, 0)
    expanded = 0
    table = Table()
    heap = []

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

def topath(note):

    path = ""

    while note.father is not None:
        path += str(note.action)
        note = note.father

    return path[::-1]



