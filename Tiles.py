import sys
from algorithm import BFS, Astar
from Astar import Astar

"""
Name: David Graber
Email: D3217453@gmail.com
Date: 18/11/2025


Main function: receives an array from command-line arguments
Converts input strings to integers, represents the initial puzzle state
Runs BFS and A* algorithms on the puzzle and prints the results
"""

def main(arr):
    # Convert input to integers for puzzle representation
    arr = [int(i) for i in arr]

    # Run BFS
    path, Expanded, cost = BFS(arr)
    printer("BFS", path, Expanded, cost)

    # Run A*
    path, Expanded, cost = Astar(arr)
    printer("A*", path, Expanded, cost)


"""
Helper function to print algorithm results
Algorithm: name of the algorithm used
path: the sequence of moves taken to reach the goal
Expanded: number of nodes expanded during search
cost: total path length (number of moves)
"""

def printer(Algorithm, path, Expanded, cost):
    print(f"Algorithm: {Algorithm}")
    print(f"Path:", end='')
    for i in path:
        print(f" {i}", end='')
    print("")
    print(f"Length: {cost}")
    print(f"Expanded: {Expanded}")
    print()

if __name__ == "__main__":
    main(sys.argv[1:])
