'''
Project 1 - Search-based solutions for static Pac-Man game.

bfs.py: breadth-first search solutions for problem.

Subject:
    MC906/MO416 - Introduction to Artificial Intelligence.
Authors:
    Daniel Helú Prestes de Oliveira - RA 166215
    Eduardo Barros Innarelli        - RA 170161
    Matheus Rotta Alves             - RA 184403
    Victor Ferreira Ferrari         - RA 187890
    Vinícius Couto Espindola        - RA 188115

University of Campinas - UNICAMP - 2020

Last Modified: 01/05/2020.
'''

import numpy as np
from PacProblemNoMaze import PacProblem
from sys import argv

# Add aima folder to PYTHONPATH environment variable.
from search import breadth_first_tree_search, breadth_first_graph_search

def bfs_pacman():
    maze = np.array([['|', '|', '|', '|', '|'],
                ['|', '.', '.', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['.', '.', '|', '.', '.'],
                ['|', '.', '.', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '|', '|', '|', '|']]).astype('bytes')

    # Get maze from file
    # Careful: uses a lot of RAM
    if len(argv) > 1:
        maze = np.genfromtxt(argv[1], dtype=str, delimiter=1).astype('bytes')
    
    # Create Problem
    init = (5,2)
    goal = (15,3)
    prob = PacProblem(init, goal, maze)
    assert maze[goal] == b'.' or maze[goal] == b' ', "Goal unreachable."
    
    # Solve with BFS
    # Problem: explodes too fast 
    final_state = breadth_first_tree_search(prob)
    print('Actions (Tree): ', final_state.solution())
    print('Score (Tree): ', -1*final_state.path_cost)
    
    # Graph: Only works without maze in state.
    final_state = breadth_first_graph_search(prob)
    print('Actions (Graph): ', final_state.solution())
    print('Score (Graph): ', -1*final_state.path_cost)

if __name__ == '__main__':
    bfs_pacman()
