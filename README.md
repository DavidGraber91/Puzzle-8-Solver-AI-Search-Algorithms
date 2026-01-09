# Puzzle-8-Solver-AI-Search-Algorithms
## Overview

This project was developed as part of an Introduction to Artificial Intelligence course.
It implements classic state-space search algorithms to solve the 8-puzzle problem, demonstrating hands-on experience with Python, algorithm design, heuristics, and data structures.

The project includes implementations of:
Breadth-First Search (BFS)
A* search with heuristic optimization

## Problem Description – The 8 Puzzle

The 8-puzzle consists of a 3×3 board with tiles numbered from 0 to 8, where 0 represents the empty space.
Goal state:

0 1 2
3 4 5
6 7 8

The task is to reach the goal configuration by sliding tiles into the empty space using the minimum number of moves.

## Implemented Algorithms
### Breadth-First Search (BFS)

Explores the state space level by level
Guarantees an optimal solution
High memory consumption
Used mainly as a reference baseline

### A* Search

Uses a priority queue (heapq)
Evaluation function:

f(n) = g(n) + h(n)

Combines actual path cost with heuristic estimation
Efficient and optimal for this problem

## Heuristic Function

The A* algorithm uses a custom heuristic based on:

### Manhattan Distance

For each tile, the distance between its current position and its goal position is calculated.
The sum of all tile distances forms the base heuristic.

### Backtracking Penalty

An additional penalty is applied if a move appears to undo previous progress.
This discourages unnecessary back-and-forth moves and improves search efficiency.
The heuristic is:
Admissible
Informed

## Hash Table for Visited States

To avoid exploring the same puzzle state multiple times, the project uses a custom hash table:
Each puzzle state is mapped to a hash index based on selected tile positions.
Each bucket stores a list of states with the same hash value.
If a state already exists:
The algorithm keeps the version with the lower cost
Higher-cost duplicates are ignored
This significantly improves performance and prevents infinite loops.

## Technical Highlights

Object-oriented state representation
Priority queue optimization using heapq
Custom heuristic design
Custom hash table for state deduplication
Clear separation between logic, data structures, and execution

## How to Run
Requirements

Python 3.x
NumPy

Install dependencies:
pip install numpy

Run example:

python Tiles.py 1 4 0 5 8 2 3 6 7

### Technical Highlights:
Object-oriented state representation
Priority queue optimization using heapq
Custom heuristic design
Custom hash table for state deduplication
Clear separation between logic, data structures, and execution
